# API CALENDÁRIO

## OBJETIVO DA APLICAÇÃO

A API fornece um calendário completo, incluindo feriados, para um ano ou mês específico. Para isso, ela integra a [`Brasil API`](https://brasilapi.com.br/docs#tag/Feriados-Nacionais), que oferece dados sobre feriados existentes apenas por ano, mas não disponibiliza o calendário completo. Esta API preenche essa lacuna, permitindo que os usuários acessem um calendário abrangente com todas as datas relevantes.

## SUMÁRIO

- [`INSTALAÇÃO`](#INSTALAÇÃO)
- [`API EXTERNA`](#API-EXTERNA)
- [`LINKS DO PROJETO`](#LINKS-DO-PROJETO)

## INSTALAÇÃO

### PRÉ-REQUISITOS

- Instalar o Docker na máquina

### PARA INICIAR A API CALENDÁRIO

Digite os seguintes comandos no terminal:

```
git clone https://github.com/luscianaderose/api_calendario
docker build -t nome_da_imagem .
docker run -d -p 5000:5000 nome_da_imagem
```

Para acessar no navegador:
http://localhost:5000/

## API EXTERNA

a api externa é a Brasil API que fornece informações gerais sobre o brasil como mapeadomento de cep ou feriados.

Sobre a API:

- `Documentação`: https://brasilapi.com.br/docs
- `Licença`: Licença MIT
- ``Cadastro`: Não aplicável

Rotas Utilizadas:

- `Documentação`: https://brasilapi.com.br/docs#tag/Feriados-Nacionais
- `https://brasilapi.com.br/api/feriados/v1/{ano}`: retorna todos os feriados por ano

## LINKS DO PROJETO

Os demais repositórios associados a este projetos podem ser consultados em:

- [front_recepcao](https://github.com/luscianaderose/front_recepcao)
- [api_recepcao](https://github.com/luscianaderose/api_recepcao)
- [deploy_recepcao](https://github.com/luscianaderose/deploy_recepcao)
- [figma](https://www.figma.com/proto/4WaxuFjrOhR8aIHIlHXuIP/prj-recepcao-cefp-01?node-id=0-1&t=XGYyK7bsqyAa5qK2-1)
