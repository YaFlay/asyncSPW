

class PaymentParameters:
    def __init__(self, amount: int, redirectUrl: str, webhookUrl: str, data: str) -> str:
        """Создание параметров ссылки на оплату

        Args:
            amount (int): Стоимость покупки в АРах.
            redirectUrl (str): URL страницы, на которую попадет пользователь после оплаты.
            webhookUrl (str): URL, куда наш сервер направит запрос, чтобы оповестить ваш сервер об успешной оплате.
            data (str): Строка до 100 символов, сюда можно помеcтить любые полезные данных.
        Returns:
            str: Ссылка на транзакцию
        """
        
        
        
        

        self.amount = amount
        self.redirectUrl = redirectUrl
        self.webhookUrl = webhookUrl
        self.data = data

    def __str__(self):
        return f'''
                amount: {self.amount}
                redirectUrl: {self.redirectUrl}
                webhookUrl: {self.webhookUrl}
                data: {self.data}
               '''


class TransactionParameters:
    def __init__(self, receiver: str, amount: int, comment: str = 'No comment') -> None:
        """Отправка транзакции
            
        

        Args:
            receiver (str): Номер карты на которую будет совершена транзакция.
            amount (int): Сумма транзакции.
            comment (str, optional): Комментарий к транзакции. Стандартно 'No comment'.
        Returns:
            None
        """

        self.receiver = receiver
        self.amount = amount
        self.comment = comment

    def __str__(self):
        return f'''
                receiver: {self.receiver}
                amount: {str(self.amount)}
                comment: {self.comment}
               '''