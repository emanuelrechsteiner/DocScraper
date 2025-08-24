# DocScraper Deployment Guide

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment Scenarios](#deployment-scenarios)
- [Monitoring](#monitoring)
- [Scaling](#scaling)
- [Backup and Recovery](#backup-and-recovery)
- [Security](#security)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

#### Minimum Requirements
- **CPU**: 4 cores (2.0 GHz+)
- **RAM**: 8 GB
- **Storage**: 50 GB available
- **OS**: macOS 12+, Ubuntu 20.04+, Windows 10+
- **Python**: 3.8+

#### Recommended Requirements
- **CPU**: 8+ cores (3.0 GHz+)
- **RAM**: 16 GB
- **Storage**: 200 GB SSD
- **OS**: macOS 13+, Ubuntu 22.04+
- **Python**: 3.10+

### Software Dependencies

```bash
# System packages
apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    build-essential \
    libssl-dev \
    libffi-dev

# Python packages (see requirements.txt)
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-org/docscraper.git
cd docscraper
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Run tests
python -m pytest tests/

# Check installation
python -c "from DocPostProcessor import DocumentPostProcessor; print('✅ Installation successful')"
```

---

## Configuration

### 1. Environment Setup

Create `.env` file in project root:

```bash
# .env
OPENAI_API_KEY=sk-your-api-key-here

# Optional configurations
DOC_PROCESSOR_MAX_WORKERS=25
DOC_PROCESSOR_BATCH_SIZE=50
DOC_PROCESSOR_CHECKPOINT_INTERVAL=100
DOC_PROCESSOR_OUTPUT_BASE=/Volumes/NvME-Satechi/VectorDatabase

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/docscraper/processor.log

# Performance
ENABLE_PROFILING=false
MEMORY_LIMIT_GB=8
```

### 2. Application Configuration

Create `config.yaml`:

```yaml
# config.yaml
processing:
  max_workers: 25
  batch_size: 50
  checkpoint_interval: 100
  timeout_seconds: 15
  retry_attempts: 3
  
openai:
  model: "gpt-4o-mini"
  max_completion_tokens: 20
  temperature: 0.3
  timeout: 15
  rate_limit_rpm: 500
  
output:
  base_directory: "/data/vector_database"
  create_dated_folders: true
  flatten_structure: true
  compression: true
  
monitoring:
  enable_metrics: true
  metrics_port: 9090
  health_check_port: 8080
```

### 3. Logging Configuration

Create `logging.conf`:

```ini
[loggers]
keys=root,docprocessor,openai

[handlers]
keys=console,file,error_file

[formatters]
keys=standard,detailed

[logger_root]
level=INFO
handlers=console,file

[logger_docprocessor]
level=DEBUG
handlers=file,error_file
qualname=docprocessor
propagate=0

[logger_openai]
level=WARNING
handlers=file
qualname=openai
propagate=0

[handler_console]
class=StreamHandler
level=INFO
formatter=standard
args=(sys.stdout,)

[handler_file]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=detailed
args=('/var/log/docscraper/app.log', 'a', 10485760, 5)

[handler_error_file]
class=handlers.RotatingFileHandler
level=ERROR
formatter=detailed
args=('/var/log/docscraper/error.log', 'a', 10485760, 5)

[formatter_standard]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[formatter_detailed]
format=%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s
```

---

## Deployment Scenarios

### Local Development

```bash
# Quick start
python DocPostProcessor.py /path/to/docs /path/to/output --use-llm

# With GUI
python DocPostProcessorGUI.py
```

### Production Server

#### 1. Systemd Service (Linux)

Create `/etc/systemd/system/docscraper.service`:

```ini
[Unit]
Description=DocScraper Processing Service
After=network.target

[Service]
Type=simple
User=docscraper
Group=docscraper
WorkingDirectory=/opt/docscraper
Environment="PATH=/opt/docscraper/venv/bin"
ExecStart=/opt/docscraper/venv/bin/python /opt/docscraper/DocPostProcessor.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable docscraper
sudo systemctl start docscraper
sudo systemctl status docscraper
```

#### 2. Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m -u 1000 docscraper && \
    chown -R docscraper:docscraper /app

USER docscraper

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import sys; sys.exit(0)"

ENTRYPOINT ["python", "DocPostProcessor.py"]
```

Build and run:

```bash
# Build image
docker build -t docscraper:latest .

# Run container
docker run -d \
  --name docscraper \
  -v /data/input:/input \
  -v /data/output:/output \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  docscraper:latest /input /output --use-llm
```

#### 3. Kubernetes Deployment

Create `k8s-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: docscraper
spec:
  replicas: 3
  selector:
    matchLabels:
      app: docscraper
  template:
    metadata:
      labels:
        app: docscraper
    spec:
      containers:
      - name: processor
        image: docscraper:latest
        resources:
          requests:
            memory: "4Gi"
            cpu: "2"
          limits:
            memory: "8Gi"
            cpu: "4"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: docscraper-secrets
              key: openai-api-key
        volumeMounts:
        - name: data
          mountPath: /data
        - name: checkpoints
          mountPath: /checkpoints
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: docscraper-data
      - name: checkpoints
        persistentVolumeClaim:
          claimName: docscraper-checkpoints
```

### Cloud Deployment

#### AWS Lambda

```python
# lambda_handler.py
import json
import boto3
from DocPostProcessor import DocumentPostProcessor

def lambda_handler(event, context):
    # Get input from S3
    s3 = boto3.client('s3')
    bucket = event['bucket']
    key = event['key']
    
    # Process document
    processor = DocumentPostProcessor(
        input_dir=f"s3://{bucket}/{key}",
        output_dir=f"s3://{bucket}/processed/",
        api_key=os.environ['OPENAI_API_KEY']
    )
    
    result = processor.process_all_documents()
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
```

---

## Monitoring

### 1. Prometheus Metrics

```python
# metrics.py
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
documents_processed = Counter('documents_processed_total', 'Total processed documents')
processing_time = Histogram('processing_duration_seconds', 'Processing time')
active_workers = Gauge('active_workers', 'Number of active workers')
checkpoint_saves = Counter('checkpoint_saves_total', 'Total checkpoint saves')

# Start metrics server
start_http_server(9090)
```

### 2. Health Checks

```python
# health.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '2.0.0',
        'uptime': get_uptime(),
        'memory_usage': get_memory_usage()
    })

@app.route('/ready')
def ready():
    # Check dependencies
    checks = {
        'database': check_database(),
        'openai_api': check_openai(),
        'disk_space': check_disk_space()
    }
    
    if all(checks.values()):
        return jsonify({'status': 'ready', 'checks': checks}), 200
    else:
        return jsonify({'status': 'not ready', 'checks': checks}), 503
```

### 3. Logging Aggregation

```yaml
# filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/docscraper/*.log
  multiline.pattern: '^\d{4}-\d{2}-\d{2}'
  multiline.negate: true
  multiline.match: after

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "docscraper-%{+yyyy.MM.dd}"
```

---

## Scaling

### Horizontal Scaling

```python
# distributed_processor.py
from celery import Celery

app = Celery('docscraper', broker='redis://localhost:6379')

@app.task
def process_document_batch(batch):
    processor = DocumentPostProcessor()
    return processor.process_batch(batch)

def distribute_processing(documents, num_workers=10):
    # Split into batches
    batch_size = len(documents) // num_workers
    batches = [documents[i:i+batch_size] 
               for i in range(0, len(documents), batch_size)]
    
    # Submit to workers
    jobs = [process_document_batch.delay(batch) for batch in batches]
    
    # Collect results
    results = [job.get() for job in jobs]
    return merge_results(results)
```

### Vertical Scaling

```bash
# Optimize Python performance
export PYTHONOPTIMIZE=2
export PYTHONHASHSEED=0

# Use PyPy for better performance
pypy3 DocPostProcessor.py /input /output

# Enable multiprocessing
export DOC_PROCESSOR_USE_MULTIPROCESSING=true
export DOC_PROCESSOR_PROCESS_COUNT=8
```

---

## Backup and Recovery

### Checkpoint Strategy

```bash
#!/bin/bash
# backup_checkpoints.sh

CHECKPOINT_DIR="/data/checkpoints"
BACKUP_DIR="/backup/docscraper"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup
tar -czf "$BACKUP_DIR/checkpoint_$DATE.tar.gz" "$CHECKPOINT_DIR"

# Keep only last 7 days
find "$BACKUP_DIR" -name "checkpoint_*.tar.gz" -mtime +7 -delete

# Sync to S3
aws s3 sync "$BACKUP_DIR" "s3://backup-bucket/docscraper/"
```

### Recovery Procedure

```python
# recovery.py
import glob
import json

def find_latest_checkpoint(checkpoint_dir):
    """Find the most recent checkpoint."""
    checkpoints = glob.glob(f"{checkpoint_dir}/checkpoint_*.json")
    if not checkpoints:
        return None
    
    latest = max(checkpoints, key=os.path.getctime)
    return latest

def recover_from_failure():
    """Recover processing from last checkpoint."""
    checkpoint = find_latest_checkpoint("/data/checkpoints")
    
    if checkpoint:
        print(f"Recovering from {checkpoint}")
        processor = DocumentPostProcessor()
        processor.load_checkpoint(checkpoint)
        processor.resume_processing()
    else:
        print("No checkpoint found, starting fresh")
        start_fresh_processing()
```

---

## Security

### 1. API Key Management

```python
# secure_config.py
from cryptography.fernet import Fernet
import keyring

class SecureConfig:
    def __init__(self):
        self.cipher = Fernet(self.get_encryption_key())
    
    def get_encryption_key(self):
        # Get or create encryption key
        key = keyring.get_password("docscraper", "encryption_key")
        if not key:
            key = Fernet.generate_key().decode()
            keyring.set_password("docscraper", "encryption_key", key)
        return key.encode()
    
    def get_api_key(self):
        # Retrieve encrypted API key
        encrypted = keyring.get_password("docscraper", "openai_api_key")
        if encrypted:
            return self.cipher.decrypt(encrypted.encode()).decode()
        return None
    
    def set_api_key(self, api_key):
        # Store encrypted API key
        encrypted = self.cipher.encrypt(api_key.encode()).decode()
        keyring.set_password("docscraper", "openai_api_key", encrypted)
```

### 2. Input Validation

```python
# validation.py
import os
import magic

def validate_input_file(file_path):
    """Validate input file before processing."""
    
    # Check file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    max_size = 100 * 1024 * 1024  # 100MB
    if os.path.getsize(file_path) > max_size:
        raise ValueError(f"File too large: {file_path}")
    
    # Check file type
    allowed_types = ['text/plain', 'text/markdown', 'text/html']
    file_type = magic.from_file(file_path, mime=True)
    if file_type not in allowed_types:
        raise ValueError(f"Invalid file type: {file_type}")
    
    return True
```

### 3. Rate Limiting

```python
# rate_limiter.py
from functools import wraps
import time

class RateLimiter:
    def __init__(self, calls_per_minute=60):
        self.calls_per_minute = calls_per_minute
        self.calls = []
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove old calls
            self.calls = [c for c in self.calls if now - c < 60]
            
            # Check rate limit
            if len(self.calls) >= self.calls_per_minute:
                sleep_time = 60 - (now - self.calls[0])
                time.sleep(sleep_time)
            
            # Record call
            self.calls.append(now)
            
            return func(*args, **kwargs)
        return wrapper

# Usage
@RateLimiter(calls_per_minute=500)
async def call_openai_api(prompt):
    return await client.chat.completions.create(...)
```

---

## Troubleshooting

### Common Issues and Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| **Out of Memory** | Process killed, OOM errors | Reduce batch_size, increase swap |
| **API Rate Limits** | 429 errors from OpenAI | Implement exponential backoff |
| **Slow Processing** | <10 docs/sec | Increase max_workers |
| **Checkpoint Corruption** | JSON decode errors | Use backup checkpoint |
| **Network Timeouts** | Connection errors | Increase timeout, add retries |
| **Disk Space** | No space left errors | Clean old checkpoints, compress output |

### Debug Commands

```bash
# Check system resources
htop
df -h
free -h

# Monitor processing
tail -f /var/log/docscraper/app.log

# Check process status
ps aux | grep DocPostProcessor

# Test OpenAI connection
python -c "from openai import OpenAI; client = OpenAI(); print(client.models.list())"

# Validate checkpoint
python -c "import json; json.load(open('checkpoint.json'))"
```

### Performance Profiling

```python
# profile_processor.py
import cProfile
import pstats

def profile_processing():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run processing
    processor = DocumentPostProcessor()
    processor.process_all_documents()
    
    profiler.disable()
    
    # Save stats
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.dump_stats('processing_profile.stats')
    stats.print_stats(20)

# Analyze with snakeviz
# pip install snakeviz
# snakeviz processing_profile.stats
```

---

## Maintenance

### Regular Tasks

```yaml
# maintenance-cronjob.yaml
daily:
  - clean_old_checkpoints: "0 2 * * *"
  - backup_database: "0 3 * * *"
  - rotate_logs: "0 4 * * *"

weekly:
  - update_dependencies: "0 5 * * 0"
  - security_scan: "0 6 * * 0"
  - performance_report: "0 7 * * 0"

monthly:
  - full_backup: "0 8 1 * *"
  - capacity_planning: "0 9 1 * *"
  - cost_analysis: "0 10 1 * *"
```

---

## Support

- **Documentation**: [https://docs.docscraper.io](https://docs.docscraper.io)
- **Issues**: [https://github.com/your-org/docscraper/issues](https://github.com/your-org/docscraper/issues)
- **Community**: [https://discord.gg/docscraper](https://discord.gg/docscraper)
- **Commercial Support**: support@docscraper.io

---

*Last updated: August 2024*
