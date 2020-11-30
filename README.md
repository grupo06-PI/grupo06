# grupo06 <br>
Repositório do Grupo 06 para o Projeto Integrador 4º semestre de Sistemas de Informação  <br>
Responsáveis por informatizar a Pastelaria do Zé e o processo de controle de fiados<br>

## Integrantes:
1. Eliza Muniz de Souza
1. Lucas Vinicius Peixer Vieira
1. Matheus Bandeira
1. Nicolas Adams Diniz
1. Victor Stache Perin

## Desenvolvimento Web
Aplicar os conhecimentos adquiridos no semestre para implementar uma aplicação web que seja capaz de informatizar os processos da pastelaria do Zé ajudando-o a controlar o processo de fiados.
Regras do negócio foram definidas depois de algumas conversas com o Zé o que ele nos solicitou foi:

- Acesso disponível em:
  -Televisores
  -Smartphones
  -Microcomputadores
  -Etc
  
- Cadastro de Funcionários e Clientes com permissão por grupo
  -Funcionários:
    - Grupo 01: Admin
      -Acesso Irrestrito a todas as funcionalidades
    - Grupo 02: Atendimento Balcão
      -Abre nova comanda
      -insere produtos na comanda
  -Clientes:
    - Grupo 03: Consulta seu histórico de consumo
    -SE Cliente for mensalista(fiado):
      - Possuir obrigatoriamente no cadastro: cpf, senha, data de pagamento
      
- Cadastro de Produtos
  - Devem obrigatoriamente possuir um nome e valor, imagem do produto
  
- Cadastro Consumo/Comanda
As comandas serão placas de acrílico com numeração individual gravada em um QR Code ou Código de Barras
  - Atendente ABRE uma nova comanda
    - Programa valida se a comanda já não está em uso {teve consumo anterior e não foi finalizada/fechada pelo CAIXA}
    - Caso já esteja, deve ser descartada e encaminhada para o usuário do CAIXA
  - Atendente através de um terminal no balcão, vai lançando os produtos e quantidades consumidas pelo cliente
    - Deve ser armazenado o funcionário que realizou o lançamento dos produtos na comanda, lembrando que um mesmo cliente pode ser atendido por diferentes funcionários

  - Atendente entrega a COMANDA numerada para o cliente
  - Novos consumos deverão ser lançados na mesma comanda
  
- Caixa/Pagamentos
  - Recebimento à Vista
    - Abre a comanda e mostra em tela para o cliente os produtos {incluindo foto}, quantidades consumidas e o valor total
    - Não é obrigatória a identificação do cliente
    - Pode conceder desconto
    - Registra o funcionário que recebeu
    - Registra o pagamento da comanda como à Vista
    - Baixa a comanda, alterando seus status para fechada
  -Cadastro de FIADO
    - Abre a Comanda e mostra em tela para o cliente os produtos {incluindo foto}, quantidades consumidas e o valor total
    - Busca e seleciona o cliente
    - Valida se o cliente está apto para fazer FIADO
      - Habilitado para realizar FIADO
      - Não está inadimplente: Todo consumo dos 30 dias anteriores a data de pagamento informada pelo cliente em seu cadastro
    - Para marcar como fiado, o cliente digita seu CPF e SENHA para confirmar que o conteúdo da comanda em seu FIADO
    - Comanda deve ficar com os dados do cliente registrado e com status de FIADO
  - Recebimento FIADO
    - Seleciona o cliente
    - Programa lista todas as comandas do cliente que estão em aberto, destacando as que eventualmente estiverem vencidas
      - Nas comandas vencidas, o sistema deve realizar o cálculo do juro com base na quantidade de dias em atraso, devendo apresentar em tela esses dois valores também
      - O valor da taxa diária de juros vem de um parâmetro do programa
    - O caixa vai selecionando as comandas que o cliente deseja pagar e o programa já vai atualizando e mostrando:
      - Valor dos juros, se existir atraso
      - Valor da multa, se existir atraso
      - Valor total
    - Pode conceder desconto
    - Registra o funcionário que recebeu
    - Registra o pagamento das comandas como Fiado
    - Altera o status da comanda atrelando o id do pagamento ao seu status do pagamento
    - Ao finalizar gera um comprovante de pagamento, com o detalhamento das comandas pagas. Podendo ou não ser impresso!
    
- Lista de Produtos e valores dinâmica para TV
  - O cliente fez o investimento em uma Smart TV de 50” e já fixou na área de alcance visual dos clientes. Ele quer o seguinte:
    - Ficar alternando de forma dinâmica produtos e valores da pastelaria
    - Poder fazer agrupamento de produtos, por exemplo, sempre que aparecer o pastel de queijo aparecer também o choco leite e um pastel doce
    - Ter como definir, por produto e por agrupamento, o tempo que vai ficar aparecendo em tela, por exemplo, naquela semana ele está com um estoque de queijo que pretende gastar, então em todos os produtos dele que vai queijo ele quer dar um destaque maior 
    
- Armazenamento de log
  - Para efeitos de auditoria, dever obrigatoriamente ter armazenamento em LOG
    - Todas as operações que realizem alteração no BD
    - Login e Logout
    - Erros/Exceções
    
- Relatórios / Dashboard
    - Comandas abertas
    - Clientes inadimplentes
    - Pagamentos à Vista
    - Pagamentos Fiado
    - etc.

## Engenharia de Software
- Levantamento de requisitos: Usuário (Funcionais e não funcionais)
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Requisitos%20do%20usu%C3%A1rio%20Vers%C3%A3o%201.13.09.doc
- Levantamento de requisitos: Sistema (Funcionais e não funcionais)
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Requisitos%20do%20usu%C3%A1rio%20Vers%C3%A3o%201.13.09.doc
- Histórias de Usuário e critérios de aceitação
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Product%20Backlog%20-%20Pastelaria%20do%20Z%C3%A9.doc
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Requisitos%20do%20sistema%20Vers%C3%A3o%201.13.09.doc
    
- UML:
  - Diagrama de Classes
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/UML%20-%20Diagrama%20Classe.png
  - Diagrama de caso de uso
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/UML-%20Diagrama%20Caso%20de%20Uso.png
  - Diagrama de atividades
    - 
- Modelagem de Banco de Dados:
  - Conceitual
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Modelagem%20Conceitual.doc
  - Lógica
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/Modelagem%20L%C3%B3gica.doc
  - Física
    - https://github.com/grupo06-PI/grupo06/blob/master/EngenhariaSoftware/modelagem%20f%C3%ADsica.sql
    
- Gerenciamento de Projeto:
  - Kanban: Utilizamos a estrutura do git para criarmos um projeto para cada disciplina, e dentro dos projetos a estrutura de Kanban automatizada, onde a cada issue criada atribuíamos a um projeto e a um status (planejado, em execução, enviado para aprovação, aprovado e concluído), a cada atualização de um dos integrantes nas issues automaticamente a "nota" atribuída no projeto era movida para seu novo status até o fechamento, facilitando o controle das atividades.
  - Interação incremental: Toda estrutura e construção do projeto foi baseada em interações onde fomos refinando a aplicação em cada etapa do projeto aplicando a metodologia SCRUM, analisando as entregas já realizadas (sprint review) e planejando como melhorias em próximos sprints (Sprint Planning Meeting) e todo processo foi incremental, uma vez que a construção da aplicação foi dividida em partes / funcionalidades.

- Arquitetura e padrões de projeto
    - Técnicas Orientada a Objeto: O projeto foi implementado utilizando a linguagem Python e toda sua estrutura foi seguindo os padrões de POO.
    - Arquitetura Cliente/Servidor: Utilizamos o padrão de projeto MVC (Model-View-Controller), onde trabalhamos com as 3 camadas na aplicação. 
        -Model: Para tratar a parte lógica que gerencia os dados.
        -View: Apresenta os dados ao usuário
        -Controller: Trata os eventos, fazendo a interlocução entre as camadas de view e model.
        
## User Experience
- Mapa de Stakeholders
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/Stakeholder%20Mapa%20-%20Pastelaria%20do%20Seu%20Z%C3%A9.docx
- Questionário / Entrevistas com Stakeholders
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/Relat%C3%B3rio%20da%20Pesquisa%20Qualitativa.docx
    - https://github.com/grupo06-PI/grupo06/blob/master/UX/Relat%C3%B3rio%20de%20Pesquisa%20Quantitativa.doc
- Questionário / Entrevistas com Usuários
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/Entrevista%20com%20o%20Seu%20Z%C3%A9%20-%20Luciano%20Coelho.mp4
- Desenho das Personas (Usuário)
    - https://github.com/grupo06-PI/grupo06/blob/master/UX/Link%20gr%C3%A1ficos%20pesquisa%20usu%C3%A1rios
    - https://github.com/grupo06-PI/grupo06/blob/master/UX/Persona%20I%20-%20Pastelaria%20do%20Z%C3%A9.png
    - https://github.com/grupo06-PI/grupo06/blob/master/UX/Persona%20II%20-%20Pastelaria%20do%20Z%C3%A9.png
    - 
- Fluxo de Uso / Jornada do Usuário
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Cadastro%20de%20Clientes.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Cadastro%20de%20Comandas.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Cadastro%20de%20Funcionarios.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Cadastro%20de%20Produtos.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Configura%C3%A7%C3%B5es.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Editar%20e%20Excluir%20nos%20Modulos%20de%20Cadastro.pdf
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/User%20Flow%20-%20Login%2C%20Funcionario%20acesso.pdf
- Mapa de empatia
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/Mapa%20Empatia%20-%20Grupo06.pdf
- Esboço das soluções (com descrição das soluções/diferenciais)
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/Pastelaria%20do%20Seu%20Z%C3%A9%20-%20Brainstorming.pdf
- Protótipos navegáveis em Adobe XD
    - https://xd.adobe.com/view/7e2ecfcd-6222-4262-922f-f66a6d9290e8-2b7d/
    - https://xd.adobe.com/view/9de7cd51-9307-4d18-82f1-52d7c2882fa2-c8b4/
- Teste de Usabilidade do Produto (Escala SUS)
    - https://github.com/grupo06-PI/grupo06/blob/UXVideo/UX/System%20Usability%20Scale%20-%20SUS%20Grupo%2006.xlsx
- Interface de Usuário bem Resolvida (Design Visual)
- Outras Validações de Acessibilidade
  - Site Utilizado para validar as cores para Daltonismo: https://www.color-blindness.com/coblis-color-blindness-simulator/
  - Site Utilizado para validar o contraste nos padrões W3C: https://contrastchecker.com/
