import flet as tf
 
def main(page: tf.Page):

    def route_change(e: tf.RouteChangeEvent):
        if e.route == "/register":
            page.add(tf.Text("Register!"))

        elif e.route == "/login":
            page.add(tf.Text("Login!"))           

    def go_to_register():
        page.route = "/register"
        page.update()

    def go_to_login():
        page.route = "/login"
        page.update()

    if page.client_storage.contains_key("user_data"):
        page.title = "Login | KingCart"
        page.add(tf.Text("Login_"))
        go_to_login()
    else:
        page.title = "Register | KingCart"
        page.add(tf.Text("Register_"))
        page.go("/login")

    #page.update()
    page.on_route_change = route_change
    page.title = "KingCart"
    print(page.client_user_agent)
 
tf.app(target=main, view=tf.WEB_BROWSER, port = 5000, assets_dir="assets")