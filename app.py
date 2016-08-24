import fbchat

client = fbchat.Client("khiemhuynh952@gmail.com", "emyeuquy")
friends = client.getUsers("Khiem Huynh")  # return a list of names
friend = friends[0]
sent = client.send(friend.uid, "Your Message")
if sent:
    print("Message sent successfully!")
