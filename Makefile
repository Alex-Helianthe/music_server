# Filename: Makefile

# Variables
VENV_DIR = venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip3
UVICORN = $(VENV_DIR)/bin/uvicorn
UVICORN_CMD = $(UVICORN) main:app --reload --host 0.0.0.0
SERVICE_NAME = music_server.service

# Default target
all: install run

# Create a virtual environment
$(VENV_DIR)/bin/activate: 
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies in the virtual environment
install: $(VENV_DIR)/bin/activate
	apt-get install python3-dev
	$(PIP) install -r requirements.txt
	@echo "Installation completed."
	make setup-service

# Start the server with Uvicorn
run:
	$(UVICORN_CMD)

# Restart the server
reboot:
	@echo "Restarting the server..."
	kill -HUP `pgrep uvicorn` || echo "No Uvicorn server found"
	make run

# Uninstall the virtual environment and clean up temporary files
uninstall:
	@echo "Removing the virtual environment and cleaning up temporary files..."
	rm -rf $(VENV_DIR)
	rm -rf __pycache__ .pytest_cache
	rm -rf *.pyc *.pyo
	make remove-service
	@echo "Uninstallation and cleanup completed."

# Install Bluetooth script from a GitHub repository
bluetooth:
	@echo "Downloading and installing the Bluetooth script..."
	wget https://raw.githubusercontent.com/nicokaiser/rpi-audio-receiver/main/install.sh
	bash install.sh
	@echo "Bluetooth script installation completed."

# Create a systemd service file to start the server at boot
setup-service:
	@echo "Creating systemd service to launch the server at startup..."
	sudo bash -c 'echo "[Unit]" > /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "Description=Music Server FastAPI Service" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "[Service]" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "WorkingDirectory=$$(pwd)" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "ExecStart=$$(pwd)/$(UVICORN_CMD)" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "Restart=always" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "User=$$(whoami)" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "[Install]" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo bash -c 'echo "WantedBy=multi-user.target" >> /etc/systemd/system/$(SERVICE_NAME)'
	sudo systemctl daemon-reload
	sudo systemctl enable $(SERVICE_NAME)
	sudo systemctl start $(SERVICE_NAME)
	@echo "Service created and enabled."

# Remove the systemd service
remove-service:
	@echo "Removing the systemd service..."
	sudo systemctl stop $(SERVICE_NAME) || echo "Service was not running."
	sudo systemctl disable $(SERVICE_NAME)
	sudo rm /etc/systemd/system/$(SERVICE_NAME)
	sudo systemctl daemon-reload
	@echo "Service removed."


