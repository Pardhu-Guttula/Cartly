# Epic Title: Integrate multiple payment gateways

class PaymentGatewayService:

    def __init__(self):
        self.available_gateways = ['GatewayA', 'GatewayB', 'GatewayC']

    def is_gateway_available(self, gateway: str) -> bool:
        return gateway in self.available_gateways

    def validate_payment(self, gateway: str, payment_details: dict) -> bool:
        # Implement payment validation logic for the selected gateway here
        return True