import random
from abc import ABC, abstractmethod


class Jogo(ABC):

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass

    @abstractmethod
    def pontuar(self, tentativa):
        pass


class Jogador:

    def __init__(self, nome):
        self.__nome = nome
        self.__pontuacao = 0

    def get_nome(self):
        return self.__nome

    def get_pontuacao(self):
        return self.__pontuacao

    def set_nome(self, nome):
        self.__nome = nome

    def set_pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao


class JogoAdivinhacao(Jogo):

    ranking = []

    def __init__(self, jogador):
        self.jogador = jogador
        self.numero_secreto = 0
        self.max_tentativas = 0
        self.limite_numero = 0

    def iniciar(self):
        print("\n=== JOGO DE ADIVINHAÇÃO ===")
        print(f"Jogador: {self.jogador.get_nome()}")
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (número de 1 a 10, 5 tentativas)")
        print("2 - Médio (número de 1 a 50, 7 tentativas)")
        print("3 - Difícil (número de 1 a 100, 10 tentativas)")

        while True:
            try:
                nivel = int(input("Digite o nível (1, 2 ou 3): "))
                if nivel == 1:
                    self.limite_numero = 10
                    self.max_tentativas = 5
                    break
                elif nivel == 2:
                    self.limite_numero = 50
                    self.max_tentativas = 7
                    break
                elif nivel == 3:
                    self.limite_numero = 100
                    self.max_tentativas = 10
                    break
                else:
                    print("Escolha inválida. Digite 1, 2 ou 3.")
            except ValueError:
                print("Digite apenas números.")

        self.numero_secreto = random.randint(1, self.limite_numero)

    def jogar(self):
        acertou = False

        print(f"\nAdivinhe um número entre 1 e {self.limite_numero}.")

        for tentativa in range(1, self.max_tentativas + 1):
            while True:
                try:
                    palpite = int(input(f"Tentativa {tentativa}: "))
                    if 1 <= palpite <= self.limite_numero:
                        break
                    else:
                        print(f"Digite um número entre 1 e {self.limite_numero}.")
                except ValueError:
                    print("Digite apenas números inteiros.")

            if palpite == self.numero_secreto:
                print("Parabéns! Você acertou!")
                pontos = self.pontuar(tentativa)
                self.jogador.set_pontuacao(pontos)
                acertou = True
                break
            elif palpite < self.numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")

        if not acertou:
            print(f"\nVocê não acertou. O número era {self.numero_secreto}.")
            self.jogador.set_pontuacao(0)

        print(f"Pontuação final: {self.jogador.get_pontuacao()}")

    def pontuar(self, tentativa):
        if tentativa > self.max_tentativas:
            return 0

        if self.max_tentativas == 1:
            return 10

        pontos = 10 - ((tentativa - 1) * 9) // (self.max_tentativas - 1)
        return pontos

    def salvar_ranking(self):
        JogoAdivinhacao.ranking.append(self.jogador)

    @staticmethod
    def exibir_ranking():
        print("\n=== RANKING ===")

        if len(JogoAdivinhacao.ranking) == 0:
            print("Nenhum jogador no ranking ainda.")
            return

        ranking_ordenado = sorted(
            JogoAdivinhacao.ranking,
            key=lambda jogador: jogador.get_pontuacao(),
            reverse=True
        )

        for posicao, jogador in enumerate(ranking_ordenado, start=1):
            print(f"{posicao}º - {jogador.get_nome()} : {jogador.get_pontuacao()} pontos")


def main():
    while True:
        nome = input("\nDigite o nome do jogador: ").strip()

        while nome == "":
            print("O nome não pode ficar vazio.")
            nome = input("Digite o nome do jogador: ").strip()

        jogador = Jogador(nome)
        jogo = JogoAdivinhacao(jogador)

        jogo.iniciar()
        jogo.jogar()
        jogo.salvar_ranking()
        jogo.exibir_ranking()

        continuar = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nEncerrando o jogo...")
            break


if __name__ == "__main__":
    main()
