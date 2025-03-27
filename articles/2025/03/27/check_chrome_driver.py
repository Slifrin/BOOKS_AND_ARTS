import undetected_chromedriver as uc


def main():
    driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.get('https://apps.supremecourt.az.gov/publicaccess/')
    driver.save_screenshot('nowsecure.png')


if __name__ == '__main__':
    main()