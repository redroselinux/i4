import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def main():
    # Get current username dynamically
    username = os.getlogin()

    # Load and blur the image
    img = Image.open("./currentscreen.png").convert("RGBA")
    blurred = img.filter(ImageFilter.GaussianBlur(radius=5))

    # Prepare to draw text
    draw = ImageDraw.Draw(blurred)

    # Choose a font and size
    try:
        font_user = ImageFont.truetype("DejaVuSans.ttf", 40)
        font_pass = ImageFont.truetype("DejaVuSans.ttf", 30)
    except IOError:
        font_user = ImageFont.load_default()
        font_pass = ImageFont.load_default()

    # Text to draw
    user_text = username
    pass_text = "Enter password to unlock (just start typing)"

    # Image size
    width, height = blurred.size

    # Calculate text sizes using textbbox
    user_bbox = draw.textbbox((0, 0), user_text, font=font_user)
    user_w, user_h = user_bbox[2] - user_bbox[0], user_bbox[3] - user_bbox[1]

    pass_bbox = draw.textbbox((0, 0), pass_text, font=font_pass)
    pass_w, pass_h = pass_bbox[2] - pass_bbox[0], pass_bbox[3] - pass_bbox[1]

    # Position text horizontally centered at top
    margin_top = 20
    spacing = 10
    user_pos = ((width - user_w) // 2, margin_top)
    pass_pos = ((width - pass_w) // 2, margin_top + user_h + spacing)

    # Draw text with shadow
    shadow_offset = 2
    draw.text((user_pos[0]+shadow_offset, user_pos[1]+shadow_offset), user_text, font=font_user, fill="black")
    draw.text(user_pos, user_text, font=font_user, fill="white")
    draw.text((pass_pos[0]+shadow_offset, pass_pos[1]+shadow_offset), pass_text, font=font_pass, fill="black")
    draw.text(pass_pos, pass_text, font=font_pass, fill="white")

    # Save image
    blurred.save("./currentscreen.png")

if __name__ == "__main__":
    main()

