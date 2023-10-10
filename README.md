[Working Link](https://scenestripp.streamlit.app/)

### How the App Works
The app offers an intuitive, user-friendly interface, guiding users through a simple journey:
 - **Upload:** A user begins by uploading their desired image. We focused on supporting common formats like PNG, JPG, and JPEG to cater to a wide audience.
 - **Remove Background:** With just a click, the app processes the image, and using advanced AI algorithms, it separates the foreground (the main subject) from the background.
 - **Choose a New Background:** After removing the original backdrop, the user is presented with an option to pick a new background color. This addition ensures that users have the flexibility not just to remove, but also to replace backgrounds as they see fit. A real-time preview is showcased to provide instant feedback.
 - **Download:** Once satisfied, users can download their transformed image with a transparent background or with their chosen color. This provides versatility in how the edited image can be used further.


### Tech Stack Used in the App
The app leverages a blend of modern technologies to ensure efficiency and user satisfaction:
 - **Streamlit:** A game-changer for rapid app development in Python. It offers a sleek interface without the overhead of complex web frameworks.
 - **Python:** The backbone of the app, allowing for the seamless integration of various libraries and ensuring robust image processing.
 - **PIL (Pillow):** A powerful imaging library in Python, it provides the tools necessary for image manipulations like opening, saving, and editing images.
 - **rembg:** An AI-based library optimized for background removal. Its neural network model has been trained on vast datasets to understand and differentiate between foregrounds and backgrounds in diverse image scenarios.