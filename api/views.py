# api/views.py
import os
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
from .models import AICompletion
from django.core.paginator import Paginator

# Initialize client (it will also pick up OPENAI_API_KEY from env)
client = OpenAI(api_key="")

@api_view(['POST'])
def ai_completion(request):
    """
    POST JSON: { "prompt": "Your question here" }
    """
    prompt = request.data.get('prompt', '').strip()
    if not prompt:
        return Response({'error': 'No prompt provided.'}, status=400)

    # Get request metadata
    ip_address = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Start timing
    start_time = time.time()
    
    try:
        # Use the Responses API to generate a completion
        resp = client.responses.create(
            model="gpt-4.1-nano",        # or any model you have access to
            input='Write a short story about '+prompt + ' in 100 words',           # your text prompt
            temperature=0.7         # optional: control randomness
        )
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Extract tokens used safely
        tokens_used = None
        if hasattr(resp, 'usage') and resp.usage:
            if hasattr(resp.usage, 'total_tokens'):
                tokens_used = resp.usage.total_tokens
            elif hasattr(resp.usage, 'get'):
                tokens_used = resp.usage.get('total_tokens')
        
        # Save to database
        ai_completion = AICompletion.objects.create(
            prompt=prompt,
            response=resp.output_text,
            model_used="gpt-4.1-nano",
            temperature=0.7,
            tokens_used=tokens_used,
            processing_time=processing_time,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        return Response({
            'response': resp.output_text,
            'completion_id': ai_completion.id,
            'processing_time': round(processing_time, 3),
            'tokens_used': tokens_used
        })

    except Exception as e:
        # Save failed request to database
        processing_time = time.time() - start_time
        AICompletion.objects.create(
            prompt=prompt,
            response=f"Error: {str(e)}",
            model_used="gpt-4.1-nano",
            temperature=0.7,
            processing_time=processing_time,
            ip_address=ip_address,
            user_agent=user_agent
        )
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def completions_list(request):
    """
    GET: Retrieve list of stored AI completions with pagination
    Query parameters: page (default: 1), limit (default: 10)
    """
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    
    # Get all completions ordered by creation date
    completions = AICompletion.objects.all()
    
    # Paginate results
    paginator = Paginator(completions, limit)
    page_obj = paginator.get_page(page)
    
    # Prepare response data
    completions_data = []
    for completion in page_obj:
        completions_data.append({
            'id': completion.id,
            'prompt': completion.prompt,
            'response': completion.response,
            'model_used': completion.model_used,
            'temperature': completion.temperature,
            'tokens_used': completion.tokens_used,
            'processing_time': completion.processing_time,
            'ip_address': completion.ip_address,
            'created_at': completion.created_at.isoformat(),
        })
    
    return Response({
        'completions': completions_data,
        'pagination': {
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'total_count': paginator.count,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
        }
    })

def get_client_ip(request):
    """Get the client's IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
