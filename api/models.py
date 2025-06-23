from django.db import models
from django.utils import timezone

class AICompletion(models.Model):
    """
    Model to store AI completion prompts and responses
    """
    prompt = models.TextField(help_text="The user's input prompt")
    response = models.TextField(help_text="The AI's generated response")
    model_used = models.CharField(max_length=50, default="gpt-4.1", help_text="The AI model used for generation")
    temperature = models.FloatField(default=0.7, help_text="Temperature setting for response generation")
    tokens_used = models.IntegerField(null=True, blank=True, help_text="Number of tokens used in the request")
    processing_time = models.FloatField(null=True, blank=True, help_text="Time taken to process the request in seconds")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the request")
    user_agent = models.TextField(blank=True, help_text="User agent of the request")
    created_at = models.DateTimeField(default=timezone.now, help_text="When the completion was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the record was last updated")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "AI Completion"
        verbose_name_plural = "AI Completions"

    def __str__(self):
        return f"Completion {self.id} - {self.prompt[:50]}..."

    @property
    def prompt_preview(self):
        """Return a shortened version of the prompt for display"""
        return self.prompt[:100] + "..." if len(self.prompt) > 100 else self.prompt

    @property
    def response_preview(self):
        """Return a shortened version of the response for display"""
        return self.response[:100] + "..." if len(self.response) > 100 else self.response
