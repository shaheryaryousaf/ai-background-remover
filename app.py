import streamlit as st
from PIL import Image
from io import BytesIO
from rembg import remove

# Page Config
st.set_page_config(page_title="Scene Strip - A Background Removal AI App")
st.title("Scene Strip")
uploaded_file = st.file_uploader(
    "Upload an image", type=['png', 'jpg', 'jpeg'])


# Remove Image Background
def remove_background(input_image):
    buffered = BytesIO()
    input_image.save(buffered, format="PNG")
    img_nobg = remove(buffered.getvalue())
    return Image.open(BytesIO(img_nobg))


# Set New Background to the Image
def apply_background(img_no_bg, color):
    new_bg_image = Image.new("RGB", img_no_bg.size, color)
    new_bg_image.paste(img_no_bg, mask=img_no_bg.split()[3])
    return new_bg_image


if uploaded_file:
    image = Image.open(uploaded_file)

    if "image_no_bg" not in st.session_state:
        if st.button('Remove Background'):
            st.session_state.image_no_bg = remove_background(image)

    if "image_no_bg" in st.session_state:
        color = st.color_picker("Pick a background color", "#ffffff")
        final_img = apply_background(st.session_state.image_no_bg, color)
        st.image(final_img, caption="Image with new background.",
                 use_column_width=True)

        # Create columns for the buttons
        col1, col2, col3 = st.columns(3)

        # Place buttons in the defined columns
        with col1:
            # Button to download transparent image
            transparent_buffered = BytesIO()
            st.session_state.image_no_bg.save(
                transparent_buffered, format="PNG")
            st.download_button(
                label="Download Transparent Image",
                data=transparent_buffered.getvalue(),
                file_name="image_with_no_bg.png",
                mime="image/png"
            )

        with col2:
            # Button to download image with colored background
            colored_buffered = BytesIO()
            final_img.save(colored_buffered, format="PNG")
            st.download_button(
                label="Download Image",
                data=colored_buffered.getvalue(),
                file_name="image_with_colored_bg.png",
                mime="image/png"
            )

        with col3:
            # Reset button
            if st.button("Reset"):
                if "image_no_bg" in st.session_state:
                    del st.session_state.image_no_bg
                uploaded_file = None
                st.experimental_rerun()
    else:
        st.image(image, caption="Uploaded Image.", use_column_width=True)
