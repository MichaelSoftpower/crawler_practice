def login(page, username, password):
    page.fill("input[name=username]", username)    
    page.fill("input[name=password]", password)
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")