from .models import PageVisit

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request
        response = self.get_response(request)
        
        # Simple tracking (exclude admin, analytics, static, media)
        if not any(request.path.startswith(prefix) for prefix in ['/admin/', '/analytics/', '/static/', '/media/']):
            # Get IP (simplistic)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            try:
                PageVisit.objects.create(
                    path=request.path,
                    ip_address=ip,
                    user_agent=request.META.get('HTTP_USER_AGENT', '')
                )
            except Exception:
                # Fail silently on Vercel (Read-only DB)
                pass
            
        return response
