from dash import html

def TabButton(title: str, id: str, icon: str):
    return html.Div(html.A([
                    html.I(className=f'fa-solid {icon} fa-xl'),
                    html.Br(),
                    title
                ], id=id, href='#', className='btn'), className='footer-tab')