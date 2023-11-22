from functools import wraps
from user_agents import parse
import logging

logger = logging.getLogger("my_logger")


def log_event(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        user_agent_string = request.META.get("HTTP_USER_AGENT", "unknown")
        user_agent = parse(user_agent_string)
        browser = user_agent.browser.family
        os = user_agent.os.family
        device = user_agent.device.family
        logger.info(f"Browser: {browser}, OS: {os}, Device: {device}")

        return func(self, request, *args, **kwargs)

    return wrapper
