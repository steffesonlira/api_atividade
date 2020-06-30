from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael',idade=25)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Steffeson').first()
    pessoa.idade = 25
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Steffeson').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    exclui_pessoa()
    consulta_pessoas()
    #altera_pessoa()
