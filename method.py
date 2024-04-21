class Phone:
    price  = 10000
    color = "Black"
    brand = "Nokia"

    def call(self):
        print("Call One Person ")
    def send_sms(self, number,sms):
        print(f"SMS Send successful{number}, This sms is :{sms}")

my_phone = Phone()

my_phone.call()
my_phone.send_sms(3135453,"I love You DS")

