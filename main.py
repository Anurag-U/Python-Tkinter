
from libraries import *

global key
dict = {"key":""}


def Received(key):
    print("\n\n")
    print("██████╗ ███████╗ ██████╗███████╗██╗██╗   ██╗███████╗██████╗ ")
    print("██╔══██╗██╔════╝██╔════╝██╔════╝██║██║   ██║██╔════╝██╔══██╗")
    print("██████╔╝█████╗  ██║     █████╗  ██║██║   ██║█████╗  ██████╔╝")
    print("██╔══██╗██╔══╝  ██║     ██╔══╝  ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print("██║  ██║███████╗╚██████╗███████╗██║ ╚████╔╝ ███████╗██║  ██║")
    print("╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝")
    print("\n\n")
    print("---------------------------WELCOME--------------------------")
    print("In order to receive the file you must have the same exact")
    print("         key the sender used while trasmitting.")
    print("------------------------------------------------------------")

    pattern = re.compile(".*[+#].*")

    # key = ""
    # while bool(pattern.match(key)) or key == "":
    
    
    # key = dict["key"]
    print(key)

    while key == "":
        key = input("Enter a non empty private key: ")


    fileTopic = "/{0}/file".format(key)
    fileinfoTopic = "/{0}/fileinfo".format(key)
    receiverChannelTopic = "/{0}/receiverChannel".format(key)
    senderChannelTopic = "/{0}/senderChannel".format(key)

    filename = "nofilename"
    file = None
    cnx = False
    # counter = 1
    sent = False

    def establish_connection(threadName, delay):
        print("Waiting for sender to connect...")
        while not cnx:
            mqttc.publish(senderChannelTopic, "0")
            time.sleep(delay)

    def on_connect(client, userdata, flags, rc):
        client.subscribe(fileTopic)
        client.subscribe(fileinfoTopic)
        client.subscribe(receiverChannelTopic)
        

    def on_message(client, userdata, message):
        global filename
        global file
        global cnx
        global counter

        if message.topic == receiverChannelTopic:
            msg = str(message.payload.decode("utf-8","ignore"))
            if msg == "0":
                print("Sender connected.")

                cnx = True
                
            elif msg == "1":
                print("File received successfully!")
                publish.single(senderChannelTopic, "1", hostname="broker.emqx.io")
                file.close()
                exit()

        elif message.topic == fileinfoTopic:
            print("File Info:")
            fileinfo=json.loads(message.payload.decode("utf-8", "ignore"))
            print(" - Name : {0}\n - Size : {1} KB\n - Number of chunks : {2}".format(fileinfo["name"], fileinfo["size"], fileinfo["chunks"]))
            filename=fileinfo['name']
            print("Begin file writing...")
            file=open(filename, "wb")

        elif message.topic == fileTopic:
            print("\tReceiving chunk ({0})...".format(counter))
            file.write(message.payload)
            counter += 1

    mqttc=mqtt.Client()
    mqttc.on_connect=on_connect
    mqttc.on_message=on_message
    mqttc.connect("broker.emqx.io",1883,60)
    

    thread.start_new_thread(establish_connection, ("Connection-Establish", 5))

    mqttc.loop_forever()


def send(key):
    
    print("\n\n")
    print("███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ ")
    print("██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗")
    print("███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝")
    print("╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")
    print("███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║")
    print("╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print("\n\n")
    print("---------------------WELCOME---------------------")
    print("Make sure the file you are about to transmit is")
    print("         located in the same directory.")
    print("-------------------------------------------------")

    # pattern = re.compile(".*[+#].*")
    # if key:
    #     print(key)
    # key = ""


    print(key)
    # key = dict["key"]
    while key == "":
        key = input("Enter a non empty private key: ")

    fileTopic = "/{0}/file".format(key)
    fileinfoTopic = "/{0}/fileinfo".format(key)
    senderChannelTopic = "/{0}/senderChannel".format(key)
    receiverChannelTopic = "/{0}/receiverChannel".format(key)

    def on_connect(client, userdata, flags, rc):
        client.subscribe(senderChannelTopic)
        print("Waiting for the receiver to connect...")

    def on_message(client, userdata, message):
        if message.topic == senderChannelTopic:
            msg = str(message.payload.decode("utf-8","ignore"))
            if msg == "0":
                print("Receiver is connected.")
                publish.single(receiverChannelTopic, "0", hostname="broker.emqx.io")
                
                transmit()
            elif msg == "1":
                print("SUCCESS")
                exit()

    def transmit():
         
        # frame = Frame(parent, width=500,height=300,bg='yellow')
        # frame.place(x=0,y=0)
        # send_data = tk.Button(frame,text="SEND", fg="green",width=15, height=5)

        # send_data.place(x=10,y=20)
        counter = 1
        fileinfo = {}
        print("select file to open")
        # filename = input("Enter filename with extension: ")
        filename = fd.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        f=open(filename, "rb") 
        print("File opened.")

        filesize = round(os.stat(filename).st_size / 1024.0, 2)
        nbrChunks = math.ceil(os.stat(filename).st_size / 10240)

        fileinfo["name"] = os.path.basename(filename)
        fileinfo["size"] = filesize
        fileinfo["chunks"] = nbrChunks

        print("Sending file info...")
        publish.single(fileinfoTopic, json.dumps(fileinfo), hostname="broker.emqx.io")

        print("Starting file data transmission")
        fileContent = f.read(10240)
        while(fileContent):
            byteArr = bytearray(fileContent)

            print("\tSending chunk ({0})...".format(counter))
            publish.single(fileTopic, byteArr, hostname="broker.emqx.io")

            fileContent = f.read(10240)
            counter += 1

        print("File sent successfully!")
        publish.single(receiverChannelTopic, "1", hostname="broker.emqx.io")
        print("Waiting for receiver AKN...")

    mqttc=mqtt.Client()
    mqttc.on_connect=on_connect
    mqttc.on_message=on_message
    mqttc.connect("broker.emqx.io",1883,60)
    mqttc.loop_forever()




# Creating mainscreen
class MainScreen:

    def __init__(self,root):
        self.root = root
        self._key1=""
        self._key2=""
        
    def main(self):
        print("Main Screen Opened")
        frame = Frame(self.root, width=500,height=300,bg='sky blue')
        frame.place(x=0,y=0)
        # Send data button
        send_data = tk.Button(frame,
                    text="SEND",
                    fg="black",
                    command=lambda: self.open_sender_pin(),
                    width=15,
                    height=5)

        send_data.place(x=120,y=110)

        # Recieve data button
        receive_data= tk.Button(frame, 
                        text="RECIEVED", 
                        fg="black",
                        command=lambda: self.open_reciever_pin(),
                        # command=lambda: open_recieved_Window(),
                        width=15,
                        height=5)
        receive_data.place(x=250,y=110)



    # Input pin method for sender
    def open_sender_pin(self):
        print("SEND button clicked")

        print("sender pin frame opened")
        frame4 =Frame(self.root,width=500,height=300,bg='sky blue').place(x=0,y=0)
        
        self.passw_label = tk.Label(frame4, text = 'Enter a Password',background="sky blue" ).place(x=180,y=80)
        # self.passw_label.grid(row=1,column=0)

        self.key1=tk.Entry(frame4)
        self.key1.place(x=160,y=100)

        sub_btn=tk.Button(frame4,text = 'Submit', command=lambda: self.send_submit())
        sub_btn.place(x=200,y=120)

        back_btn= Button(frame4,text = "Back",command=lambda: self.main())
        back_btn.place(x=20,y=200)


    # Input pin method for sender
    def open_reciever_pin(self):
        print("SEND button clicked")
        print("reciever pin frame opened")

        frame3 =Frame(self.root,width=500,height=300,bg='sky blue').place(x=0,y=0)
        # frame3.place(x=0,y=0)

        self.passw_label = tk.Label(frame3, text = 'Enter a Password',background="sky blue" ).place(x=180,y=80)
        # passw_label.grid(row=1,column=0)

        self.key2=tk.Entry(frame3)
        self.key2.place(x=160,y=100)

        sub_btn=tk.Button(frame3,text = 'Submit', command =lambda: self.rec_submit())
        sub_btn.place(x=200,y=120)
        back_btn= Button(frame3,text = "Back",command=lambda: self.main())
        back_btn.place(x=20,y=200)
   
   
   # submit method of sender
    def send_submit(self):
        print("submit button clicked")

        self._key1 = self.key1.get()
        
        # key2 = self.key2.get()
        print(self._key1)
        send(self._key1)
        # print(key2)
        

   # submit method of reciever
    def rec_submit(self):
        print("submit button clicked")

        # key1 = self.key1.get()
        
        self._key2 = self.key2.get()
        # print(key1)
        print(self._key2)
        Received(self._key2)
    




counter = 1
# main()

if __name__ =='__main__':

    parent = Tk()
    parent.geometry("500x300")
    parent.title('ShareIn'.center(130))

    screen = MainScreen(parent)
    screen.main()
    parent.mainloop()
