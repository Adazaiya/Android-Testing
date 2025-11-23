# Project Overview

The project explores a demonstration of Android testing tools and frameworks, focusing on Espresso and Appium.

# Prerequisites
Android Studio

JDK 11 or higher

Node.js 18+ and npm

Python 3.10+

# Project Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Android_Testing.git
cd Android_Testing
```

## 2. Install Android Studio and SDK
1. Download and install Android Studio
2. Open Android Studio and install Android SDK
3. Set environment variables
   ```bash
   export ANDROID_HOME=$HOME/Library/Android/sdk
   export ANDROID_SDK_ROOT=$HOME/Library/Android/sdk
   export PATH=$PATH:$ANDROID_HOME/platform-tools
   export PATH=$PATH:$ANDROID_HOME/tools
   ```
   Add these to ``` ~/.zshsrc  ```
   ```bash
   echo 'export ANDROID_HOME=$HOME/Library/Android/sdk' >> ~/.zshrc
   echo 'export ANDROID_SDK_ROOT=$HOME/Library/Android/sdk' >> ~/.zshrc
   echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> ~/.zshrc
   source ~/.zshrc
   ```
   Verify installation
   ```bash
   adb --version
   echo $ANDROID_HOME
    ```
## 3. Running Appium Tests

1. Start Appim Server
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export ANDROID_SDK_ROOT=$HOME/Library/Android/sdk

# Start Appium
appium
 ```
2. Run Appium Test
```bash
cd appium-tests
python3 login_test.py
```


   
   
