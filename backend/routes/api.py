# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

api_bp = Blueprint('api', __name__)

def register_blueprints(app):
    from admin_dashboard.controllers import admin_dashboard_bp
    from analytics_and_reporting.controllers import analytics_reporting_bp
    from checkout_process.controllers import checkout_process_bp
    from marketplace_expansion.controllers import marketplace_expansion_bp
    from mobile_optimization.controllers import mobile_optimization_bp
    from product_catalog.controllers import product_catalog_bp
    from product_promotions_and_discounts.controllers import promotions_discounts_bp
    from shopping_cart_and_wishlist.controllers import shopping_cart_wishlist_bp
    from user_accounts.controllers import user_accounts_bp
    from user_authentication.controllers import user_authentication_bp

    app.register_blueprint(admin_dashboard_bp, url_prefix='/api/admin_dashboard')
    app.register_blueprint(analytics_reporting_bp, url_prefix='/api/analytics_reporting')
    app.register_blueprint(checkout_process_bp, url_prefix='/api/checkout_process')
    app.register_blueprint(marketplace_expansion_bp, url_prefix='/api/marketplace_expansion')
    app.register_blueprint(mobile_optimization_bp, url_prefix='/api/mobile_optimization')
    app.register_blueprint(product_catalog_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(promotions_discounts_bp, url_prefix='/api/promotions_discounts')
    app.register_blueprint(shopping_cart_wishlist_bp, url_prefix='/api/shopping_cart_wishlist')
    app.register_blueprint(user_accounts_bp, url_prefix='/api/user_accounts')
    app.register_blueprint(user_authentication_bp, url_prefix='/api/user_authentication')