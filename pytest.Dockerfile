# Start with a base image containing Python
FROM python:3.11.4

# Set the working directory within the Docker container
WORKDIR /app

# Copy the source code from the Jenkins workspace into the Docker image
COPY . /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Selenium WebDriver and related dependencies
# You might also need additional packages like ChromeDriver or GeckoDriver
RUN apt-get update && \
    apt-get install -y unzip wget && \
    # Install Chrome
    wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i /tmp/chrome.deb && \
    apt-get install -f -y && \
    rm /tmp/chrome.deb && \
    # Install ChromeDriver
    CHROMEDRIVER_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Set the command to run the tests
CMD ["pytest"]

