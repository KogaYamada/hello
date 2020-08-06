def announce(f):
  def wrapper():
    print("about to run the function...")
    f()
    print("done with the funciton.")
  return wrapper

@announce
def hello():
  print("Hello, World!!")

hello()
