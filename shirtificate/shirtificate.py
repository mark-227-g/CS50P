from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 0, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)

def main():

    myname=input("Name: ")
    print(myname)

    shirtpdf = PDF()
    shirtpdf.add_page(orientation = "portrait" ,format="A4")
    shirtpdf.image("shirtificate.png",y=20,w=shirtpdf.epw)
    shirtpdf.set_font("helvetica", size=24,style="B")
    shirtpdf.set_text_color(r=255,g=255,b=255)
    shirtpdf.cell(0,100, f"{myname} took CS50",align="C")
    shirtpdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()