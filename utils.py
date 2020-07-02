from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=25)
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


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('joao', '123')
    insere_usuario('Jose', '321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # exclui_pessoa()
    # consulta_pessoas()
    # altera_pessoa()
