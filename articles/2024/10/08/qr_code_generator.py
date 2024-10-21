import qrcode



def simple_example():
    img = qrcode.make('Some data here')
    print(type(img))

    img.show()

def more_advanced_usage():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://en.wikipedia.org/wiki/Continuous_Liquid_Interface_Production')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

def main() -> None:
    print(f'Hello main from : {__file__}')

    more_advanced_usage()


if __name__ == '__main__':
    main()