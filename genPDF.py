from reportlab.pdfgen import canvas

def gerarPDF(lista):
    try:
        nomenclatura_pdf = input('Informe ou nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nomenclatura_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x,'{} : {}'.format(nome, idade))
        pdf.setTitle(nomenclatura_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750,'Lista -')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245, 724, 'Siga e compartilhe com os amigos!')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nomenclatura_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nomenclatura_pdf))

lista = {'@gusdevs': 'gusdevs.com'}
gerarPDF(lista)