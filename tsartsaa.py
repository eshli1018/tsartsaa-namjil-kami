from Toolbox import color, clear, slow, box, ask

learned=[]
player = {
  "name": "Царцаа Намжил",
  "learned" : [],
  "stage" : 1,
} 
slow("Сайн уу!")
slow("Царцаа Намжилын аялал")
slow("Эрт урьд цагт тэнэг хүн байжээ...")

name = input("Чиний нэр хэн бэ? ") 
slow("Сайн уу, " + name + "!")
slow(f"{name}, чи өнөөдөр Царцаа Намжил болж алялах болно.")

#12*6=72mur 6mur+12mur=18mur => 72mur code-g 18mur code hylbarchilj baigaa gesen ug
def header(title):
  print("===  " + title + "  ===")

def header(title) :
  """Дэлгэцийг цэвэрлээд, гарчгийн хүрээнд хэвлэнэ.
  (12-р хичээлд бид үүнийг сайжруулж явц + сурсан тарнийг нэмнэ.)"""
  clear()
  box([title])
  
def ask_choice():
  """"1" эсвэл  "2" гэсэн ЗӨВ сонголт авах хүртэл дахин дахин асууна."""
  while True:
    choice = ask(" Чиний сонголт (1 эсвэл 2) :") #1
    if choice == "1" or choice == "2":
      return choice # choice = 
    print(color(" Зөвхөн 1 эсвэл 2 гэж бичнэ үү.","red"))



def hiid():
  header("1-р хэсэг: Хийдэд")
  slow("Багш <<Замдаа тохиолдсон бүгдийг ажигла>> гэв.")

  choices = ["Толгой дохин , замдаа бүгдийг АЖИГЛАХААР шийдэх.","<<Ажиглаад нэмэргүй>> гээд олон ном заа гэж зүтгэх."]
  for i in range(len(choices)):
    print(" [" + str(i + 1) + "] " + choices[i])

  choice = ask_choice() #choice=1

  if choice == "1":
   slow("Чи замд гарлаа!, Аялал үргэлжилнэ" "(зөв)" )
   learned.append("1-r hesgiig amjilttai surlaa") #utga nemdeg = append 
  elif choice == "2":
   slow("Багш чамааг хөөн, чи талд төөрч мөхөв" "буруу")


  
def har_shuvuu():
  slow("2-р хэсэг: Зам дээр — Хар шувуу ")
  header("2-р хэсэг: Зам дээр — Хар шувуу ")
  
  slow("Өндөр модон дээр том хар шувуу «увааг — увааг» гэж дуугарав.")
  choices = [" «Бараан шувуу вуааг вуааг» гэж ажиглан тогтоох", " Чулуу шидэж хөөх"]
  daw = len(choices)
  for i in range(daw):
    slow("[" + str(i + 1) + "]" + choices[i])

  choice = ask_choice() 

  if choice == "1":
   slow("Чи дуу авиаг цээжлэн цааш явав. Аялал үргэлжилнэ! (зөв)")
   learned.append("2-r heseg surlaa Чи дуу авиаг цээжлэн цааш явав. Аялал үргэлжилнэ!")
  elif choice == "2":
   slow("Чи цээжлэх зүйлээ алдав, (буруу)")

def main():
  hiid()
  har_shuvuu()
  # print(scene["title"])
  # print(scene["choices"][0]["text"])
  print("sursan hicheeluud:", learned)

main()
  
