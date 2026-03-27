import datetime
import os
import sys
import logging

# Setup logging to file
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"server_{datetime.datetime.now().strftime('%Y%m%d')}.log")

# Configure Python logging to write to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8')
    ]
)

logger = logging.getLogger("llmproxy")
logger.info(f"--- Server starting at {datetime.datetime.now().isoformat()} ---")

try:
    from server import app
    import uvicorn
    
    logger.info("Imports OK, starting uvicorn...")
    
    # Run without uvicorn's default logging config
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info", log_config=None)
except Exception as e:
    logger.exception(f"FATAL: {e}")
    raise
