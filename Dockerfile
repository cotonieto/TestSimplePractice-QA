# Usa una imagen base de Python para Windows
FROM python:3.9-windowsservercore

# Configuración de variables de entorno para Chrome
ENV CHROME_VERSION="135.0.7049.41"
ENV CHROMEDRIVER_VERSION="135.0.7049.41"

# Descarga e instala Chrome
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
    Invoke-WebRequest -Uri "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$env:CHROME_VERSION/win64/chrome-win64.zip" -OutFile "chrome.zip"; \
    Expand-Archive -Path "chrome.zip" -DestinationPath "C:\chrome"; \
    Remove-Item -Path "chrome.zip"

# Descarga e instala ChromeDriver
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
    Invoke-WebRequest -Uri "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$env:CHROMEDRIVER_VERSION/win64/chromedriver-win64.zip" -OutFile "chromedriver.zip"; \
    Expand-Archive -Path "chromedriver.zip" -DestinationPath "C:\chromedriver"; \
    Remove-Item -Path "chromedriver.zip"; \
    $env:PATH = 'C:\chromedriver\chromedriver-win64;' + $env:PATH; \
    [Environment]::SetEnvironmentVariable('PATH', $env:PATH, [EnvironmentVariableTarget]::Machine)

# Configura el directorio de trabajo
WORKDIR C:/app
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir selenium python-dotenv

# Configura las variables de entorno para Chrome
ENV PATH="C:\chrome\chrome-win64;C:\chromedriver\chromedriver-win64;${PATH}"

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]