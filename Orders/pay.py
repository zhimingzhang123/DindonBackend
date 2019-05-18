from alipay import AliPay

from Utils.keys.Key import AliPayKey

alipay = AliPay(
    # 默认回调url
    app_private_key_string=AliPayKey.app_private_key,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=AliPayKey.alipay_public_key,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=True  # 默认False
)

alipay.api_alipay_trade_wap_pay(
    out_trade_no="",
    total_amount=100.0,  # 价格

)
