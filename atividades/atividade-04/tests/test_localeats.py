import pytest
from playwright.sync_api import sync_playwright


# Responsável: Rafaela Martins
URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"


@pytest.fixture
def pagina_local_eats():
    """Abre a tela de autenticação do LocalEats."""
    with sync_playwright() as playwright:
        try:
            navegador = playwright.chromium.launch(headless=True)
        except Exception as erro:
            pytest.skip(
                "Chromium do Playwright não está instalado. "
                "Execute: python -m playwright install chromium. "
                f"Detalhe: {erro}"
            )

        pagina = navegador.new_page()
        try:
            resposta = pagina.goto(
                URL_LOGIN,
                wait_until="domcontentloaded",
                timeout=30000
            )
            assert resposta is not None, "A navegação não retornou uma resposta HTTP."
            assert resposta.status < 400, (
                f"A página de login retornou status HTTP {resposta.status}."
            )
            yield pagina
        finally:
            navegador.close()


def test_login_exibe_campos_e_permite_preencher_credenciais(pagina_local_eats):
    """TF01: verifica os campos e o preenchimento da tela de login."""
    pagina = pagina_local_eats

    assert pagina.locator("#loginForm").is_visible()
    assert pagina.locator("#showLoginBtn").is_visible()

    campo_email = pagina.locator("#loginEmail")
    campo_senha = pagina.locator("#loginPassword")

    assert campo_email.is_visible()
    assert campo_senha.is_visible()

    campo_email.fill("rafaela.teste@example.com")
    campo_senha.fill("SenhaTeste123!")

    assert campo_email.input_value() == "rafaela.teste@example.com"
    assert campo_senha.input_value() == "SenhaTeste123!"


def test_alternar_entre_login_e_cadastro(pagina_local_eats):
    """TF02: verifica a alternância entre os formulários de login e cadastro."""
    pagina = pagina_local_eats

    pagina.locator("#showRegisterBtn").click()

    assert pagina.locator("#registerForm").is_visible()
    assert pagina.locator("#loginForm").is_hidden()
    assert pagina.locator("#regName").is_visible()
    assert pagina.locator("#regEmail").is_visible()
    assert pagina.locator("#regPassword").is_visible()

    pagina.locator("#showLoginBtn").click()

    assert pagina.locator("#loginForm").is_visible()
    assert pagina.locator("#registerForm").is_hidden()
