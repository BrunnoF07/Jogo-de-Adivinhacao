# 🎯 Jogo de Adivinhação em Python

Projeto simples desenvolvido em **Python**, utilizando conceitos de **Programação Orientada a Objetos (POO)** e aplicando os princípios **SOLID**.

---

## 📌 Sobre o projeto

O jogo consiste em adivinhar um número aleatório entre **1 e 100**, dentro de um número limitado de tentativas.

O objetivo principal é demonstrar boas práticas de desenvolvimento, organização de código e uso de conceitos fundamentais da programação orientada a objetos.

---

## 🧠 Conceitos aplicados

### 🔹 Abstração

A classe base `Jogo` define métodos genéricos como `iniciar()` e `jogar()`, servindo como base para outras implementações.

### 🔹 Encapsulamento

Uso de atributos privados, como `__numero_secreto`, garantindo maior segurança e controle sobre os dados.

### 🔹 Herança

A classe `JogoAdivinhacao` herda características da classe `Jogo`, promovendo reutilização de código.

### 🔹 Polimorfismo

Os métodos `iniciar()` e `jogar()` são sobrescritos, permitindo diferentes comportamentos conforme a implementação.

### 🔹 Princípios SOLID

O projeto segue boas práticas de design de software, incluindo:

* **SRP** (Responsabilidade Única)
* **OCP** (Aberto/Fechado)
* **LSP** (Substituição de Liskov)
* **ISP** (Segregação de Interface)
* **DIP** (Inversão de Dependência)

---

## ▶️ Como executar

1. Instale o **Python** em sua máquina
2. Execute o arquivo principal:

```bash
python jogo.py
```

---

## 📂 Estrutura do projeto

```
jogo.py
README.md
```

---

## 🚀 Melhorias futuras

* Sistema de pontuação
* Ranking de jogadores
* Interface gráfica
* Níveis de dificuldade

---

## 👨‍💻 Autor

**Brunno Machado dos Santos**

---

Se quiser, posso deixar ainda mais profissional (tipo padrão GitHub com badges, prints ou GIF do jogo funcionando).
