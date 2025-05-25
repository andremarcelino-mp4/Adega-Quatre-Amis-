import customtkinter as ctk
import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="adega"
)
with conexao.cursor() as cursor:
    cursor.execute("""
        SELECT fgk_vinho FROM tbl_pedidos
    """)
    vinhos_pedidos = cursor.fetchall()
    for (id_vinho,) in vinhos_pedidos:
        cursor.execute("""
            UPDATE tbl_vinhos
            SET venda = true
            WHERE id_vinho = %s
        """, (id_vinho,))
    conexao.commit()

def janela_login():
    ctk.set_appearance_mode('dark')
    janela_login = ctk.CTk()
    janela_login.geometry('460x450')
    janela_login.title('Login Adega 4 amigos')
    janela_login.attributes("-fullscreen", True)
    frame1 = ctk.CTkFrame(janela_login, width=400, height=420)
    frame1.pack(pady=200, padx=10, anchor='center')
    frame1.pack_propagate(False)
    frame2 = ctk.CTkFrame(frame1, width=250, height=50)
    frame2.pack(pady=10, padx=10)
    frame2.pack_propagate(False)
    label1 = ctk.CTkLabel(frame2, text='Adega Quatro Amigos ', font=('arial', 20, 'bold'))
    label1.pack(pady=10)
    label_usuario = ctk.CTkLabel(frame1, text='Usuário', font=('arial', 15, 'bold'))
    label_usuario.pack(pady=2)
    campo_usuario = ctk.CTkEntry(frame1, placeholder_text='Digite o usuário')
    campo_usuario.pack(pady=8)
    label_senha = ctk.CTkLabel(frame1, text='Senha', font=('arial', 15, 'bold'))
    label_senha.pack(pady=8)
    campo_senha = ctk.CTkEntry(frame1, placeholder_text='Digite a senha', show='*')
    campo_senha.pack(pady=2)
    resultado_login = ctk.CTkLabel(frame1, text='', font=('arial', 15, 'bold'))
    resultado_login.pack(pady=10)

    cursor = conexao.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM tbl_vinhos
        WHERE venda = false
    """)
    total_vinhos = cursor.fetchone()[0]
    ctk.CTkLabel(frame1, text=f"Total de vinhos cadastrados: {total_vinhos}", font=("Arial", 13, "bold")).pack(pady=2)
    if total_vinhos < 5:
        ctk.CTkLabel(
            frame1,
            text=f"⚠ Apenas {total_vinhos} vinho(s) cadastrado(s) no estoque!",
            text_color="orange",
            font=("Arial", 14, "bold")
        ).pack(pady=2)

    

    btn_login = ctk.CTkButton(frame1, text='Login', width=200, height=30, corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          command=lambda: validar_login(campo_usuario, campo_senha, resultado_login, janela_login))
    btn_login.pack(pady=25)
  


    janela_login.mainloop()

def validar_login(campo_usuario, campo_senha, resultado_login, tela_login):
    usuario_login = campo_usuario.get()
    senha_login = campo_senha.get()
    if usuario_login == 'adega' and senha_login == '12345':
        tela_login.withdraw()
        janela_adega()
    else:
        resultado_login.configure(text='Usuário ou senha incorretos', text_color='red')
    
def janela_adega():
    janela_adega = ctk.CTk()
    ctk.set_appearance_mode('dark')
    janela_adega.geometry('800x1000')
    janela_adega.title('Adega Quatro Amigos')
    janela_adega.attributes("-fullscreen", True)
    frame_adega = ctk.CTkFrame(janela_adega, width=700, height=800, corner_radius=15)
    frame_adega.place(relx=0.5, rely=0.5, anchor='center')
    frame_adega.pack_propagate(False)
    titulo_bemvindo = ctk.CTkLabel(frame_adega, text='Bem vindo ao gerenciamento da Adega 4 amigos!', font=('Arial', 24, 'bold'))
    titulo_bemvindo.pack(pady=50, padx = 20)
    titulo2 = ctk.CTkLabel(frame_adega, text='O que deseja fazer?', font=('Arial', 20, 'bold'))
    titulo2.pack(pady=20, padx = 20)
    btn_inserir = ctk.CTkButton(frame_adega, text='Cadastrar vinho', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: inserir(conexao))
    btn_inserir.pack(pady=10, padx=10)
    btn_inserir.pack_propagate(False)
    btn_atualizar = ctk.CTkButton(frame_adega, text='Atualizar vinho', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: atualizar(conexao))
    btn_atualizar.pack(pady=10, padx=10)
    btn_atualizar.pack_propagate(False)
    btn_deletar = ctk.CTkButton(frame_adega, text='Deletar vinho',corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: deletar(conexao))
    btn_deletar.pack(pady=10, padx=10)
    btn_deletar.pack_propagate(False)
    btn_listar = ctk.CTkButton(frame_adega, text='Listar vinhos', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: listar(conexao))
    btn_listar.pack(pady=10, padx=10)
    btn_listar.pack_propagate(False)
    btn_cadastrar_fab = ctk.CTkButton(frame_adega, text='Cadastrar fabricante', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: cadastrar_fabricante(conexao))
    btn_cadastrar_fab.pack(pady=10, padx=10)
    btn_cadastrar_fab.pack_propagate(False)
    btn_deletar_fab = ctk.CTkButton(frame_adega, text='Deletar fabricante', corner_radius=10,
    fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
    width=250, height=40, command=lambda: deletar_fabricante(conexao))
    btn_deletar_fab.pack(pady=10, padx=10)
    btn_deletar_fab.pack_propagate(False)

    btn_cadastrar_pedido = ctk.CTkButton(frame_adega, text='Cadastrar pedido', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: cadastrar_pedido(conexao))
    btn_cadastrar_pedido.pack(pady=10, padx=10)
    btn_cadastrar_pedido.pack_propagate(False)
    btn_listar_pedidos = ctk.CTkButton(frame_adega, text='Listar pedidos', corner_radius=10,
                          fg_color='purple', hover_color='violet', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=lambda: listar_pedidos(conexao))
    btn_listar_pedidos.pack(pady=10, padx=10)
    btn_listar_pedidos.pack_propagate(False)
    btn_fechar = ctk.CTkButton(frame_adega, text='Fechar Programa', corner_radius=10,
                          fg_color='red', hover_color='darkred', font=('roboto', 12, 'bold'),
                          width=250, height=40, command=janela_adega.destroy)
    btn_fechar.pack(pady=30, padx=10)
    btn_fechar.pack_propagate(False)

    janela_adega.mainloop()

def cadastrar_fabricante(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Cadastrar Fabricante")
    janela.geometry("350x300")
    janela.attributes("-fullscreen", True)  

    ctk.CTkLabel(janela, text="Nome do fabricante:").pack(pady=10)
    entry_nome = ctk.CTkEntry(janela, placeholder_text="Nome do fabricante")
    entry_nome.pack(pady=5)

    ctk.CTkLabel(janela, text="País de origem:").pack(pady=10)
    entry_pais = ctk.CTkEntry(janela, placeholder_text="País de origem")
    entry_pais.pack(pady=5)

    resultado = ctk.CTkLabel(janela, text="")
    resultado.pack(pady=10)

    def salvar_fabricante():
        nome = entry_nome.get().strip()
        pais = entry_pais.get().strip()
        if not nome or not pais:
            resultado.configure(text="Preencha todos os campos.", text_color="red")
            return
        try:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tbl_fabricantes (nome_fabricante, pais_origem) VALUES (%s, %s)",
                    (nome, pais)
                )
                conexao.commit()
            resultado.configure(text="Fabricante cadastrado com sucesso!", text_color="green")
            entry_nome.delete(0, 'end')
            entry_pais.delete(0, 'end')
        except Exception as e:
            resultado.configure(text=f"Erro: {e}", text_color="red")
    ctk.CTkButton(janela, text="Salvar", command=salvar_fabricante).pack(pady=20)
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def inserir(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Inserir Vinho")
    janela.geometry("300x500")
    janela.attributes("-fullscreen", True) 

    cursor = conexao.cursor()
    cursor.execute("SELECT id_fabricante, nome_fabricante FROM tbl_fabricantes")
    fabricantes = cursor.fetchall()
    nomes_fabricantes = [f[1] for f in fabricantes]

    entry_nome = ctk.CTkEntry(janela, placeholder_text="Nome")
    entry_nome.pack(pady=10)
    entry_tipo = ctk.CTkEntry(janela, placeholder_text="Tipo")
    entry_tipo.pack(pady=10)
    entry_safra = ctk.CTkEntry(janela, placeholder_text="Safra (AAAA-MM-DD)")
    entry_safra.pack(pady=10)
    entry_quantidade = ctk.CTkEntry(janela, placeholder_text="Quantidade (ml)")
    entry_quantidade.pack(pady=10)
    entry_valor = ctk.CTkEntry(janela, placeholder_text="Valor (R$)")
    entry_valor.pack(pady=10)

    ctk.CTkLabel(janela, text="Fabricante:").pack(pady=5)
    combo_fabricante = ctk.CTkComboBox(janela, values=nomes_fabricantes)
    combo_fabricante.pack(pady=10)

    resultado = ctk.CTkLabel(janela, text="")
    resultado.pack(pady=10)
    
    def criar_vinho(conexao, nome, tipo, safra, quantidade, valor, fgk_fabricante):
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tbl_vinhos (nome_vinho, tipo_vinho, safra, quantidade, valor_vinho, fgk_fabricante) VALUES (%s, %s, %s, %s, %s, %s)",
            (nome, tipo, safra, quantidade, valor, fgk_fabricante)
        )
        conexao.commit()

    def salvar():
        try:
            nome = entry_nome.get()
            tipo = entry_tipo.get()
            safra = entry_safra.get()
            safra = datetime.strptime(str(safra), "%Y-%m-%d").date()
            quantidade = float(entry_quantidade.get()) 
            preco = float(entry_valor.get())
            fabricante_nome = combo_fabricante.get()
            fgk_fabricante = next((f[0] for f in fabricantes if f[1] == fabricante_nome), None)
            if fgk_fabricante is None:
                resultado.configure(text="Selecione um fabricante válido.", text_color="red")
                return
            criar_vinho(conexao, nome, tipo, safra, quantidade, preco, fgk_fabricante)
            resultado.configure(text="Vinho cadastrado com sucesso!", text_color="green")
        except ValueError:
            resultado.configure(text="Erro: data ou valores inválidos (use AAAA-MM-DD).", text_color="red")
        except Exception as e:
            resultado.configure(text=f"Erro: {e}", text_color="red")
        entry_nome.delete(0, 'end')
        entry_tipo.delete(0, 'end')
        entry_safra.delete(0, 'end')
        entry_quantidade.delete(0, 'end')
        entry_valor.delete(0, 'end')
    ctk.CTkButton(janela, text="Salvar", command=salvar).pack(pady=20)
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def deletar_fabricante(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Deletar Fabricante")
    janela.geometry("500x600")
    janela.attributes("-fullscreen", True)

    ctk.CTkLabel(janela, text="Digite o ID do fabricante que deseja deletar:").pack(pady=10)
    entry_id = ctk.CTkEntry(janela, placeholder_text="ID do fabricante")
    entry_id.pack(pady=5)

    ctk.CTkButton(janela, text="Confirmar", fg_color="orange", command=lambda: confirmar_delecao()).pack(pady=10)

    frame_resultados = ctk.CTkScrollableFrame(janela, label_text="Fabricantes Disponíveis")
    frame_resultados.pack(pady=10, fill="both", expand=True)

    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_fabricante, nome_fabricante, pais_origem
        FROM tbl_fabricantes
    """)
    resultados = cursor.fetchall()
    if not resultados:
        ctk.CTkLabel(frame_resultados, text="Nenhum fabricante cadastrado.").pack()
    else:
        for fab in resultados:
            texto = f"ID: {fab[0]} | Nome: {fab[1]} | País: {fab[2]}"
            ctk.CTkLabel(frame_resultados, text=texto).pack(pady=2)

    def confirmar_delecao():
        try:
            id_fab = int(entry_id.get())
            cursor = conexao.cursor()
          
            cursor.execute("SELECT COUNT(*) FROM tbl_vinhos WHERE fgk_fabricante = %s", (id_fab,))
            if cursor.fetchone()[0] > 0:
                ctk.CTkLabel(janela, text="Não é possível deletar: fabricante vinculado a vinho.", text_color="red").pack()
                return
            cursor.execute("DELETE FROM tbl_fabricantes WHERE id_fabricante = %s", (id_fab,))
            conexao.commit()
            ctk.CTkLabel(janela, text=f"Fabricante com ID {id_fab} deletado com sucesso!", text_color="green").pack()
        except ValueError:
            ctk.CTkLabel(janela, text="Por favor, digite um ID válido.", text_color="red").pack()
        except Exception as e:
            ctk.CTkLabel(janela, text=f"Erro ao deletar: {e}", text_color="red").pack()

    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def deletar(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Deletar Vinho")
    janela.geometry("500x600")
    janela.attributes("-fullscreen", True)

    ctk.CTkLabel(janela, text="Digite o ID do vinho que deseja deletar:").pack(pady=10)
    entry_id = ctk.CTkEntry(janela, placeholder_text="ID do vinho")
    entry_id.pack(pady=5)

    ctk.CTkButton(janela, text="Confirmar", fg_color="orange", command=lambda: confirmar_anulacao()).pack(pady=10)

    frame_resultados = ctk.CTkScrollableFrame(janela, label_text="Vinhos Disponíveis")
    frame_resultados.pack(pady=10, fill="both", expand=True)

    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_vinho, nome_vinho, tipo_vinho, safra 
        FROM tbl_vinhos
        WHERE venda = false
    """)
    resultados = cursor.fetchall()
    if not resultados:
        ctk.CTkLabel(frame_resultados, text="Nenhum vinho cadastrado.").pack()
    else:
        for vinho in resultados:
            texto = f"ID: {vinho[0]} | Nome: {vinho[1]} | Tipo: {vinho[2]} | Safra: {vinho[3]}"
            ctk.CTkLabel(frame_resultados, text=texto).pack(pady=2)

    def confirmar_anulacao():
        try:
            id_vinho = int(entry_id.get())
            cursor = conexao.cursor()
            cursor.execute("SELECT nome_vinho FROM tbl_vinhos WHERE id_vinho = %s AND venda = false", (id_vinho,))
            vinho = cursor.fetchone()
            if vinho:
                cursor.execute("""
                    UPDATE tbl_vinhos
                    SET venda = true
                    WHERE id_vinho = %s
                """, (id_vinho,))
                conexao.commit()
                ctk.CTkLabel(janela, text=f"Vinho com ID {id_vinho} deletado (vendido) com sucesso!", text_color="green").pack()
            else:
                ctk.CTkLabel(janela, text="ID não encontrado ou vinho já vendido.", text_color="red").pack()
        except ValueError:
            ctk.CTkLabel(janela, text="Por favor, digite um ID válido.", text_color="red").pack()
        except Exception as e:
            ctk.CTkLabel(janela, text=f"Erro ao deletar: {e}", text_color="red").pack()
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def deletar_fabricante(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Deletar Fabricante")
    janela.geometry("400x400")
    janela.attributes("-fullscreen", True)

    ctk.CTkLabel(janela, text="Digite o ID do fabricante que deseja deletar:").pack(pady=10)
    entry_id = ctk.CTkEntry(janela, placeholder_text="ID do fabricante")
    entry_id.pack(pady=5)

  
    frame_resultados = ctk.CTkScrollableFrame(janela, label_text="Fabricantes cadastrados sem vinho")
    frame_resultados.pack(pady=10, fill="both", expand=True)

    cursor = conexao.cursor()
    cursor.execute("""
        SELECT f.id_fabricante, f.nome_fabricante, f.pais_origem
        FROM tbl_fabricantes f
        LEFT JOIN tbl_vinhos v ON f.id_fabricante = v.fgk_fabricante
        WHERE v.id_vinho IS NULL
    """)
    fabricantes = cursor.fetchall()
    if not fabricantes:
        ctk.CTkLabel(frame_resultados, text="Nenhum fabricante sem vinho cadastrado.").pack()
    else:
        for fab in fabricantes:
            texto = f"ID: {fab[0]} | Nome: {fab[1]} | País: {fab[2]}"
            ctk.CTkLabel(frame_resultados, text=texto).pack(pady=2)

    resultado = ctk.CTkLabel(janela, text="")
    resultado.pack(pady=10)

    def confirmar_delecao():
        try:
            id_fab = int(entry_id.get())
            cursor = conexao.cursor()
        
            cursor.execute("SELECT COUNT(*) FROM tbl_vinhos WHERE fgk_fabricante = %s", (id_fab,))
            count = cursor.fetchone()[0]
            if count > 0:
                resultado.configure(
                    text="Não é possível deletar: este fabricante possui vinhos cadastrados.",
                    text_color="red"
                )
                return
            cursor.execute("SELECT nome_fabricante FROM tbl_fabricantes WHERE id_fabricante = %s", (id_fab,))
            fab = cursor.fetchone()
            if fab:
                cursor.execute("DELETE FROM tbl_fabricantes WHERE id_fabricante = %s", (id_fab,))
                conexao.commit()
                resultado.configure(text=f"Fabricante com ID {id_fab} deletado com sucesso!", text_color="green")
            else:
                resultado.configure(text="ID não encontrado.", text_color="red")
        except ValueError:
            resultado.configure(text="Por favor, digite um ID válido.", text_color="red")
        except Exception as e:
            resultado.configure(text=f"Erro ao deletar: {e}", text_color="red")

    ctk.CTkButton(janela, text="Deletar", fg_color="orange", command=confirmar_delecao).pack(pady=10)
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def atualizar(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Atualizar Vinho")
    janela.geometry("700x700")
    janela.attributes("-fullscreen", True)  

    ctk.CTkLabel(janela, text="Digite o ID do vinho que deseja atualizar:").pack(pady=10)
    entry_id = ctk.CTkEntry(janela, placeholder_text="ID do vinho")
    entry_id.pack(pady=5)

    ctk.CTkLabel(janela, text="Escolha o campo que deseja atualizar:").pack(pady=10)
    
    opcoes = ['nome_vinho', 'tipo_vinho', 'safra', 'quantidade', 'valor_vinho', 'fgk_fabricante']
    combo_campo = ctk.CTkComboBox(janela, values=opcoes)
    combo_campo.pack(pady=10)

    ctk.CTkLabel(janela, text="Digite o novo valor:").pack(pady=10)
    entry_novo_valor = ctk.CTkEntry(janela, placeholder_text="Novo valor")
    entry_novo_valor.pack(pady=10)

    cursor = conexao.cursor()
    cursor.execute("SELECT id_fabricante, nome_fabricante FROM tbl_fabricantes")
    fabricantes = cursor.fetchall()
    nomes_fabricantes = [f[1] for f in fabricantes]
    combo_fabricante = ctk.CTkComboBox(janela, values=nomes_fabricantes)
    combo_fabricante.pack(pady=10)
    combo_fabricante.pack_forget()  

    def on_campo_change(event=None):
        campo = combo_campo.get()
        if campo == 'fgk_fabricante':
            entry_novo_valor.pack_forget()
            combo_fabricante.pack(pady=10)
        else:
            combo_fabricante.pack_forget()
            entry_novo_valor.pack(pady=10)
    combo_campo.bind("<<ComboboxSelected>>", on_campo_change)

    ctk.CTkButton(janela, text="Atualizar", command=lambda: executar_atualizacao()).pack(pady=20)

    frame_resultados = ctk.CTkScrollableFrame(janela, label_text="Vinhos Disponíveis")
    frame_resultados.pack(pady=10, fill="both", expand=True)

    cursor.execute("""
        SELECT id_vinho, nome_vinho, tipo_vinho, safra
        FROM tbl_vinhos
        WHERE venda = false
    """)
    resultados = cursor.fetchall()
    if not resultados:
        ctk.CTkLabel(frame_resultados, text="Nenhum vinho cadastrado.").pack()
    else:
        for vinho in resultados:
            texto = f"ID: {vinho[0]} | Nome: {vinho[1]} | Tipo: {vinho[2]} | Safra: {vinho[3]}"
            ctk.CTkLabel(frame_resultados, text=texto).pack(pady=2)

    def executar_atualizacao():
        try:
            id_vinho = int(entry_id.get())
            campo = combo_campo.get()
            if campo == 'fgk_fabricante':
                nome_fab = combo_fabricante.get()
                novo_valor = next((f[0] for f in fabricantes if f[1] == nome_fab), None)
                if novo_valor is None:
                    ctk.CTkLabel(janela, text="Selecione um fabricante válido.", text_color="red").pack(pady=10)
                    return
            else:
                novo_valor = entry_novo_valor.get()
                if campo == 'quantidade' or campo == 'valor_vinho':
                    novo_valor = float(novo_valor)
            cursor = conexao.cursor()
            cursor.execute("SELECT venda FROM tbl_vinhos WHERE id_vinho = %s", (id_vinho,))
            result = cursor.fetchone()
            if not result or result[0]:
                ctk.CTkLabel(janela, text="Só é possível atualizar vinhos disponíveis (não vendidos).", text_color="red").pack(pady=10)
                return
            query = f"UPDATE tbl_vinhos SET {campo} = %s WHERE id_vinho = %s"
            cursor.execute(query, (novo_valor, id_vinho))
            conexao.commit()
            ctk.CTkLabel(janela, text="Atualizado com sucesso!", text_color="green").pack(pady=10)
        except ValueError:
            ctk.CTkLabel(janela, text="Erro: valor inválido para o campo selecionado", text_color="red").pack(pady=10)
        except Exception as e:
            ctk.CTkLabel(janela, text=f"Erro: {e}", text_color="red").pack(pady=10)

    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)
def listar(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Lista de Vinhos")
    janela.geometry("700x500")
    janela.attributes("-fullscreen", True)
    frame = ctk.CTkFrame(janela)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    scrollable = ctk.CTkScrollableFrame(frame, label_text="Vinhos cadastrados")
    scrollable.pack(padx=10, pady=10, fill="both", expand=True)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT v.id_vinho, v.nome_vinho, v.tipo_vinho, v.safra, v.quantidade, v.valor_vinho, f.nome_fabricante, f.pais_origem
        FROM tbl_vinhos v
        LEFT JOIN tbl_fabricantes f ON v.fgk_fabricante = f.id_fabricante
        WHERE v.venda = false
    """)
    vinhos = cursor.fetchall()
    if not vinhos:
        ctk.CTkLabel(scrollable, text="Nenhum vinho disponível.", text_color="red").pack(pady=10)
    else:
        for vinho in vinhos:
            texto = (
                f"ID: {vinho[0]} | Nome: {vinho[1]} | Tipo: {vinho[2]} | Safra: {vinho[3]} | "
                f"Quantidade: {vinho[4]}ml | Valor: R${vinho[5]:.2f} | "
                f"Fabricante: {vinho[6]} ({vinho[7]})"
            )
            ctk.CTkLabel(scrollable, text=texto, anchor="w", justify="left").pack(pady=5, padx=10, anchor='w')
    
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def cadastrar_pedido(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Cadastrar Pedido")
    janela.geometry("500x500")
    janela.attributes("-fullscreen", True)  

    ctk.CTkLabel(janela, text="Nome do cliente:").pack(pady=10)
    entry_cliente = ctk.CTkEntry(janela, placeholder_text="Nome do cliente")
    entry_cliente.pack(pady=5)

    ctk.CTkLabel(janela, text="Data do pedido (AAAA-MM-DD):").pack(pady=10)
    entry_data = ctk.CTkEntry(janela, placeholder_text="Data do pedido")
    entry_data.pack(pady=5)

    cursor = conexao.cursor()
    cursor.execute("SELECT id_vinho, nome_vinho, valor_vinho FROM tbl_vinhos WHERE nome_vinho IS NOT NULL AND venda = false")
    vinhos = cursor.fetchall()
    nomes_vinhos = [f"{v[1]} (R${v[2]:.2f})" for v in vinhos]

    ctk.CTkLabel(janela, text="Vinho:").pack(pady=10)
    combo_vinho = ctk.CTkComboBox(janela, values=nomes_vinhos)
    combo_vinho.pack(pady=5)

    resultado = ctk.CTkLabel(janela, text="")
    resultado.pack(pady=10)

    def salvar_pedido():
        nome_cliente = entry_cliente.get().strip()
        data_pedido = entry_data.get().strip()
        vinho_nome = combo_vinho.get()
        fgk_vinho = next((v[0] for v in vinhos if vinho_nome.startswith(v[1])), None)
        if not nome_cliente or not data_pedido or fgk_vinho is None:
            resultado.configure(text="Preencha todos os campos.", text_color="red")
            return
        try:
            data_pedido = datetime.strptime(data_pedido, "%Y-%m-%d").date()
            with conexao.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tbl_pedidos (data_pedido, nome_cliente, fgk_vinho) VALUES (%s, %s, %s)",
                    (data_pedido, nome_cliente, fgk_vinho)
                )
                
                cursor.execute("""
                    UPDATE tbl_vinhos
                    SET venda = true
                    WHERE id_vinho = %s
                """, (fgk_vinho,))
                conexao.commit()
            resultado.configure(text="Pedido cadastrado e vinho marcado como vendido!", text_color="green")
            entry_cliente.delete(0, 'end')
            entry_data.delete(0, 'end')
        except Exception as e:
            resultado.configure(text=f"Erro: {e}", text_color="red")
    ctk.CTkButton(janela, text="Salvar", command=salvar_pedido).pack(pady=20)
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

def listar_pedidos(conexao):
    janela = ctk.CTkToplevel()
    janela.title("Lista de Pedidos")
    janela.geometry("700x500")
    janela.attributes("-fullscreen", True)
    frame = ctk.CTkFrame(janela)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    scrollable = ctk.CTkScrollableFrame(frame, label_text="Pedidos cadastrados")
    scrollable.pack(padx=10, pady=10, fill="both", expand=True)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT p.id_pedido, p.data_pedido, p.nome_cliente, v.nome_vinho, v.valor_vinho
        FROM tbl_pedidos p
        LEFT JOIN tbl_vinhos v ON p.fgk_vinho = v.id_vinho
        ORDER BY p.id_pedido DESC
    """)
    pedidos = cursor.fetchall()
    if not pedidos:
        ctk.CTkLabel(scrollable, text="Nenhum pedido cadastrado.", text_color="red").pack(pady=10)
    else:
        for pedido in pedidos:
            texto = (
                f"ID: {pedido[0]} | Data: {pedido[1]} | Cliente: {pedido[2]} | "
                f"Vinho: {pedido[3]} | Valor: R${pedido[4]:.2f}" if pedido[4] is not None else
                f"ID: {pedido[0]} | Data: {pedido[1]} | Cliente: {pedido[2]} | Vinho: {pedido[3]}"
            )
            ctk.CTkLabel(scrollable, text=texto, anchor="w", justify="left").pack(pady=5, padx=10, anchor='w')
    ctk.CTkButton(janela, text="Voltar ao Menu", fg_color="gray", command=janela.destroy).pack(pady=10)

janela_login()
