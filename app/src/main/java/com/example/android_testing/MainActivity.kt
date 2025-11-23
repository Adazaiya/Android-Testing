package com.example.android_testing

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.android_testing.ui.theme.Android_TestingTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Android_TestingTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    LoginScreen()
                }
            }
        }
    }
}

@Composable
fun LoginScreen() {
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }
    var loggedIn by remember { mutableStateOf(false) }
    var welcomeMessage by remember { mutableStateOf("") }

    // Input error state
    var showError by remember { mutableStateOf(false) }

    // Theme management
    var baseThemeColor by remember { mutableStateOf(Color.White) }
    var themeColor by remember { mutableStateOf(baseThemeColor) }

    // Slider for opacity
    var opacity by remember { mutableStateOf(1f) }

    // Available themes
    val themes = listOf(
        Color.White to "Default",
        Color(0xFFBBDEFB) to "Blue",
        Color(0xFFC8E6C9) to "Green",
        Color(0xFFFFCDD2) to "Red"
    )

    // Counter state
    var counter by remember { mutableStateOf(0) }

    // --- MESSAGE STATE ---
    var message by remember { mutableStateOf("") }
    var isBold by remember { mutableStateOf(false) }
    var isItalic by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(themeColor.copy(alpha = opacity))
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        if (!loggedIn) {
            // --- LOGIN FORM ---
            Text(
                text = "Login Demo",
                fontSize = 24.sp,
                modifier = Modifier.padding(bottom = 32.dp)
            )

            OutlinedTextField(
                value = username,
                onValueChange = { username = it },
                label = { Text("Username") },
                modifier = Modifier
                    .fillMaxWidth()
                    .semantics { contentDescription = "usernameField" },
                singleLine = true
            )

            Spacer(modifier = Modifier.height(16.dp))

            OutlinedTextField(
                value = password,
                onValueChange = { password = it },
                label = { Text("Password") },
                visualTransformation = PasswordVisualTransformation(),
                modifier = Modifier
                    .fillMaxWidth()
                    .semantics { contentDescription = "passwordField" },
                singleLine = true
            )

            if (showError) {
                Text(
                    text = "Please enter username and password!",
                    color = Color.Red,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }

            Spacer(modifier = Modifier.height(24.dp))

            Button(
                onClick = {
                    if (username.isNotEmpty() && password.isNotEmpty()) {
                        loggedIn = true
                        welcomeMessage = "Welcome, $username!"
                        showError = false
                    } else {
                        showError = true
                    }
                },
                modifier = Modifier
                    .fillMaxWidth()
                    .semantics { contentDescription = "loginButton" }
            ) {
                Text("Login")
            }

        } else {
            // --- WELCOME SCREEN ---
            Text(
                text = welcomeMessage,
                fontSize = 20.sp,
                modifier = Modifier
                    .padding(bottom = 24.dp)
                    .semantics { contentDescription = "welcomeMessage" }
            )

            // --- MESSAGE INPUT ---
            OutlinedTextField(
                value = message,
                onValueChange = { message = it },
                label = { Text("Type a message") },
                modifier = Modifier
                    .fillMaxWidth()
                    .semantics { contentDescription = "messageField" }
            )

            Spacer(modifier = Modifier.height(16.dp))

            Row(horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                Button(
                    onClick = { isBold = !isBold },
                    modifier = Modifier.semantics { contentDescription = "boldButton" }
                ) {
                    Text("B")
                }
                Button(
                    onClick = { isItalic = !isItalic },
                    modifier = Modifier.semantics { contentDescription = "italicButton" }
                ) {
                    Text("I")
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            if (message.isNotEmpty()) {
                Text(
                    text = message,
                    fontSize = 18.sp,
                    color = Color.Black,
                    fontWeight = if (isBold) androidx.compose.ui.text.font.FontWeight.Bold else androidx.compose.ui.text.font.FontWeight.Normal,
                    fontStyle = if (isItalic) androidx.compose.ui.text.font.FontStyle.Italic else androidx.compose.ui.text.font.FontStyle.Normal,
                    modifier = Modifier.semantics { contentDescription = "formattedMessage" }
                )
            }

            Spacer(modifier = Modifier.height(24.dp))

            // --- THEME SELECTOR ---
            Text("Select Theme:", fontSize = 18.sp)
            Spacer(modifier = Modifier.height(16.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                themes.forEach { (color, label) ->
                    Button(
                        onClick = {
                            baseThemeColor = color
                            themeColor = color.copy(alpha = opacity)
                        },
                        modifier = Modifier.semantics { contentDescription = "theme_$label" }
                    ) {
                        Text(label)
                    }
                }
            }

            Spacer(modifier = Modifier.height(24.dp))

            // --- OPACITY SLIDER ---
            Text("Adjust Opacity: ${(opacity * 100).toInt()}%", fontSize = 16.sp)
            Slider(
                value = opacity,
                onValueChange = {
                    opacity = it
                    themeColor = baseThemeColor.copy(alpha = opacity)
                },
                valueRange = 0f..1f,
                steps = 9,
                modifier = Modifier
                    .fillMaxWidth()
                    .semantics { contentDescription = "opacitySlider" }
            )

            Spacer(modifier = Modifier.height(24.dp))

            // --- COUNTER ---
            Text("Counter: $counter", fontSize = 18.sp)
            Spacer(modifier = Modifier.height(8.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                Button(
                    onClick = { counter++ },
                    modifier = Modifier.semantics { contentDescription = "incrementButton" }
                ) {
                    Text("+")
                }
                Button(
                    onClick = { if (counter > 0) counter-- },
                    modifier = Modifier.semantics { contentDescription = "decrementButton" }
                ) {
                    Text("-")
                }
            }

            Spacer(modifier = Modifier.height(24.dp))

            // --- RESET THEME BUTTON ---
            Button(
                onClick = {
                    baseThemeColor = Color.White
                    opacity = 1f
                    themeColor = baseThemeColor.copy(alpha = opacity)
                },
                modifier = Modifier.semantics { contentDescription = "resetThemeButton" }
            ) {
                Text("Reset Theme")
            }

            Spacer(modifier = Modifier.height(16.dp))

            // --- LOGOUT BUTTON ---
            Button(
                onClick = {
                    loggedIn = false
                    username = ""
                    password = ""
                    welcomeMessage = ""
                    baseThemeColor = Color.White
                    themeColor = baseThemeColor.copy(alpha = 1f)
                    opacity = 1f
                    counter = 0
                    message = ""
                    isBold = false
                    isItalic = false
                },
                modifier = Modifier.semantics { contentDescription = "logoutButton" }
            ) {
                Text("Logout")
            }
        }
    }
}





