import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QIcon

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Ninja Games")
        self.setWindowIcon(QIcon("ninja.png"))  # Substitua pelo caminho real do ícone

        # Layout
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Widgets
        layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Senha:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Esconde a senha
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.authenticate)
        layout.addWidget(login_button)

    def authenticate(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # Lógica de autenticação (substitua pela sua lógica real)
        if self.is_valid_user(email, password):
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            # ... (abra a próxima janela ou faça o que for necessário)
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos.")

    def is_valid_user(self, email, password):
        # Implemente sua lógica de verificação de usuário aqui
        # ... (consulte o banco de dados, etc.)
        # Exemplo simples (substitua por sua lógica real)
        return email == "seu_email" and password == "sua_senha"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
