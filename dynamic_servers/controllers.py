
tasks = []

def show_tasks():
    return f"My tasks: {tasks}"

def show_home():
    return """
    <h1>Welcome to my dynamic website!</h1>
    <p>View my current <a href='/tasks'>tasks</a></p>
    """
    