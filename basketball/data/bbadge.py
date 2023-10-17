def get_badge(name):
    """
    Returns a badge image with the name of the person who completed the labyrinth.
    """
    import requests

    line1_text = name
    line2_text = 'completed the'
    line3_text = 'Data Dunkers'
    line4_text = 'Basketball Labyrinth'
    font_size = 46

    try:
        logo = 'images/bball-logo.jpg'
    except:
        from io import BytesIO
        logo_url = 'https://github.com/callysto/data-labyrinth/blob/main/basketball/images/bball-logo.jpg?raw=true'
        logo = BytesIO(requests.get(logo_url, allow_redirects=True).content)

    from PIL import Image, ImageDraw, ImageFont

    width, height = 400, 450
    background_color = (37, 38, 40)
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # draw the border
    draw.line((10, 10, 390, 10), fill=(242, 103, 34), width=3)
    draw.line((10, 10, 10, 440), fill=(242, 103, 34), width=3)
    draw.line((390, 10, 390, 440), fill=(242, 103, 34), width=3)
    draw.line((10, 440, 390, 440), fill=(242, 103, 34), width=3)

    # get the image
    image_to_embed = Image.open(logo).resize((374, 150))
    image.paste(image_to_embed, (13, 20+font_size*2+20))

    # get the font
    import requests
    import io
    r = requests.get('https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/RobotoCondensed-Regular.ttf', allow_redirects=True)
    font = ImageFont.truetype(io.BytesIO(r.content), size=font_size)

    # text positions
    line1_size = draw.textlength(line1_text, font=font)
    line2_size = draw.textlength(line2_text, font=font)
    line3_size = draw.textlength(line3_text, font=font)
    line4_size = draw.textlength(line4_text, font=font)
    line1_position = ((width - line1_size) // 2, 20)
    line2_position = ((width - line2_size) // 2, 20+font_size)
    line3_position = ((width - line3_size) // 2, 20+font_size*2+10+150)
    line4_position = ((width - line4_size) // 2, 20+font_size*3+10+150)

    # Draw the text on the image
    draw.text(line1_position, line1_text, fill=(111, 74, 158), font=font)
    draw.text(line2_position, line2_text, fill=(111, 74, 158), font=font)
    draw.text(line3_position, line3_text, fill=(142, 162, 161), font=font)
    draw.text(line4_position, line4_text, fill=(142, 162, 161), font=font)
    # add hashtag
    draw.text((330, 20+font_size*4+12+200), '#callysto', fill=(242, 103, 34), font=ImageFont.truetype(io.BytesIO(r.content), size=14))
    draw.text((21, 20+font_size*4+12+200), '#datadunkers', fill=(242, 103, 34), font=ImageFont.truetype(io.BytesIO(r.content), size=14))

    #return(image.resize((200, 225)))
    return(image)