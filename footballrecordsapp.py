import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_football_records_app import Ui_MainWindow


class FootballRecordsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.football_records = [
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "თავდამსხმელი", "record_type": "გატანილი გოლები",
             "player": "ალან შირერი", "value": 260, "description": "პრემიერ ლიგის ყველა დროის საუკეთესო ბომბარდირი."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "თავდამსმხელი", "record_type": "საგოლე გადაცემა",
             "player": "ტიერი ანრი", "value": 74,
             "description": "პრემიერ ლიგის რეკორდი საგოლე გადაცემებისთვის თავდამსხმელისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "თავდამსხმელი", "record_type": "ყვითელი ბარათი",
             "player": "უეინ რუნი", "value": 102,
             "description": "პრემიერ ლიგის რეკორდი ყვითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "თავდამსხმელი", "record_type": "წითელი ბარათი",
             "player": "დუნკან ფერგიუსონი", "value": 8,
             "description": "პრემიერ ლიგის რეკორდი წითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "ნახევარმცველი", "record_type": "გატანილი გოლები",
             "player": "ფრენკ ლემპარდი", "value": 177,
             "description": "პრემიერ ლიგის ყველა დროის საუკეთესო ბომბარდირი ნახევარმცველის პოზიციაზე."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "ნახევარმცველი", "record_type": "საგოლე გადაცემა",
             "player": "რაიან გიგზი", "value": 162, "description": "პრემიერ ლიგის ყველა დროის საუკეთესო ასისტენტი."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "ნახევარმცველი", "record_type": "ყვითელი ბარათი",
             "player": "გარეთ ბერი", "value": 128,
             "description": "პრემიერ ლიგის რეკორდი ყვითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "ნახევარმცველი", "record_type": "წითელი ბარათი",
             "player": "პატრიკ ვიეირა", "value": 8,
             "description": "პრემიერ ლიგის რეკორდი წითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მცველი", "record_type": "გატანილი გოლები",
             "player": "ჯონ ტერი", "value": 41,
             "description": "პრემიერ ლიგის რეკორდი გატანილი გოლებისთვის მცველის პოზიციაზე."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მცველი", "record_type": "საგოლე გადაცემა",
             "player": "ტრენტ ალექსანდერ-არნოლდი", "value": 64,
             "description": "პრემიერ ლიგის რეკორდი საგოლე გადაცემებისთვის მცველის პოზიციაზე."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მცველი", "record_type": "მშრალი კარი",
             "player": "რიო ფერდინანდი", "value": 100,
             "description": "პრემიერ ლიგის რეკორდი მშრალი კარისთვის მცველის პოზიციაზე (გუნდური მშრალი თამაშები)."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მცველი", "record_type": "ყვითელი ბარათი",
             "player": "ფილიპ იაგიელკა", "value": 90,
             "description": "პრემიერ ლიგის რეკორდი ყვითელი ბარათებისთვის მცველისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მცველი", "record_type": "წითელი ბარათი",
             "player": "რიჩარდ დანი", "value": 8,
             "description": "პრემიერ ლიგის რეკორდი წითელი ბარათებისთვის მცველისთვის."},
            {"championship": "ინგლისის პრემიერ ლიგა", "position": "მეკარე", "record_type": "მშრალი კარი",
             "player": "პეტერ ჩეხი", "value": 202, "description": "პრემიერ ლიგის რეკორდი მშრალი მატჩებისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "თავდამსხმელი", "record_type": "გატანილი გოლები",
             "player": "ლიონელ მესი", "value": 474, "description": "ლა ლიგის ყველა დროის საუკეთესო ბომბარდირი."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "თავდამსხმელი", "record_type": "საგოლე გადაცემა",
             "player": "ლიონელ მესი", "value": 192, "description": "ლა ლიგის ყველა დროის საუკეთესო ასისტენტი."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "თავდამსხმელი", "record_type": "ყვითელი ბარათი",
             "player": "სერხიო რამოსი", "value": 190,
             "description": "ლა ლიგის რეკორდი ყვითელი ბარათებისთვის თავდამსხმელისთვის (პირობითი)."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "თავდამსხმელი", "record_type": "წითელი ბარათი",
             "player": "დიეგო კოშტა", "value": 5,
             "description": "ლა ლიგის რეკორდი წითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "ნახევარმცველი", "record_type": "გატანილი გოლები",
             "player": "ლუი არაგონი", "value": 160,
             "description": "ლა ლიგის რეკორდი გატანილი გოლებისთვის ნახევარმცველისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "ნახევარმცველი", "record_type": "საგოლე გადაცემა",
             "player": "ხავი", "value": 129,
             "description": "ლა ლიგის რეკორდი საგოლე გადაცემებისთვის ნახევარმცველისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "ნახევარმცველი", "record_type": "ყვითელი ბარათი",
             "player": "გაბი", "value": 147,
             "description": "ლა ლიგის რეკორდი ყვითელი ბარათებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "ნახევარმცველი", "record_type": "წითელი ბარათი",
             "player": "პიტერ ლუჩინი", "value": 12, "description": "ლა ლიგის რეკორდი წითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მცველი", "record_type": "გატანილი გოლები",
             "player": "რონალდ კუმანი", "value": 67,
             "description": "ლა ლიგის რეკორდი გატანილი გოლებისთვის მცველის პოზიციაზე."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მცველი", "record_type": "საგოლე გადაცემა",
             "player": "დანი ალვეში", "value": 105,
             "description": "ლა ლიგის რეკორდი საგოლე გადაცემებისთვის მცველის პოზიციაზე."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მცველი", "record_type": "მშრალი კარი",
             "player": "დიეგო გოდინი", "value": 150,
             "description": "ლა ლიგის რეკორდი მშრალი კარისთვის მცველის პოზიციაზე (გუნდური მშრალი თამაშები)."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მცველი", "record_type": "ყვითელი ბარათი",
             "player": "სერხიო რამოსი", "value": 259,
             "description": "ლა ლიგის რეკორდი ყველაზე მეტი ყვითელი ბარათისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მცველი", "record_type": "წითელი ბარათი",
             "player": "სერხიო რამოსი", "value": 28,
             "description": "ლა ლიგის რეკორდი ყველაზე მეტი წითელი ბარათისთვის."},
            {"championship": "ესპანეთის ლა ლიგა", "position": "მეკარე", "record_type": "მშრალი კარი",
             "player": "ანდონი სუბისარეტა", "value": 233, "description": "ლა ლიგაში ყველაზე მეტი მშრალი მატჩი."},
            {"championship": "იტალიის სერია ა", "position": "თავდამსხმელი", "record_type": "გატანილი გოლები",
             "player": "სილვიო პიოლა", "value": 274, "description": "სერია A-ს ყველა დროის საუკეთესო ბომბარდირი."},
            {"championship": "იტალიის სერია ა", "position": "თავდამსხმელი", "record_type": "საგოლე გადაცემა",
             "player": "ფრანჩესკო ტოტი", "value": 103,
             "description": "სერია A-ს რეკორდი საგოლე გადაცემებისთვის თავდამსხმელისთვის."},
            {"championship": "იტალიის სერია ა", "position": "თავდამსხმელი", "record_type": "ყვითელი ბარათი",
             "player": "მასიმო ამბროზინი", "value": 120,
             "description": "სერია A-ს რეკორდი ყვითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "იტალიის სერია ა", "position": "თავდამსხმელი", "record_type": "წითელი ბარათი",
             "player": "ანტონიო კასანო", "value": 16,
             "description": "სერია A-ს რეკორდი წითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "იტალიის სერია ა", "position": "ნახევარმცველი", "record_type": "გატანილი გოლები",
             "player": "მარეკ ჰამშიკი", "value": 100,
             "description": "სერია A-ს რეკორდი გატანილი გოლებისთვის ნახევარმცველისთვის."},
            {"championship": "იტალიის სერია ა", "position": "ნახევარმცველი", "record_type": "საგოლე გადაცემა",
             "player": "ფრანჩესკო ტოტი", "value": 103,
             "description": "სერია A-ს რეკორდი საგოლე გადაცემებისთვის ნახევარმცველისთვის."},
            {"championship": "იტალიის სერია ა", "position": "ნახევარმცველი", "record_type": "ყვითელი ბარათი",
             "player": "ჯენარო გატუზო", "value": 130,
             "description": "სერია A-ს რეკორდი ყვითელი ბარათებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "იტალიის სერია ა", "position": "ნახევარმცველი", "record_type": "წითელი ბარათი",
             "player": "დანილო დ'ამბროზიო", "value": 7,
             "description": "სერია A-ს რეკორდი წითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "იტალიის სერია ა", "position": "მცველი", "record_type": "გატანილი გოლები",
             "player": "ჯაჩინტო ფაკეტი", "value": 59,
             "description": "სერია A-ს რეკორდი გატანილი გოლებისთვის მცველის პოზიციაზე."},
            {"championship": "იტალიის სერია ა", "position": "მცველი", "record_type": "საგოლე გადაცემა",
             "player": "პაოლო მალდინი", "value": 50,
             "description": "სერია A-ს რეკორდი საგოლე გადაცემებისთვის მცველის პოზიციაზე."},
            {"championship": "იტალიის სერია ა", "position": "მცველი", "record_type": "მშრალი კარი",
             "player": "ჯორჯო კიელინი", "value": 120,
             "description": "სერია A-ს რეკორდი მშრალი კარისთვის მცველის პოზიციაზე (გუნდური მშრალი თამაშები)."},
            {"championship": "იტალიის სერია ა", "position": "მცველი", "record_type": "ყვითელი ბარათი",
             "player": "პაოლო მალდინი", "value": 140,
             "description": "სერია A-ს რეკორდი ყვითელი ბარათებისთვის მცველისთვის."},
            {"championship": "იტალიის სერია ა", "position": "მცველი", "record_type": "წითელი ბარათი",
             "player": "პაოლო მალდინი", "value": 10,
             "description": "სერია A-ს რეკორდი წითელი ბარათებისთვის მცველისთვის."},
            {"championship": "იტალიის სერია ა", "position": "მეკარე", "record_type": "მშრალი კარი",
             "player": "ჯანლუიჯი ბუფონი", "value": 285, "description": "სერია A-ში ყველაზე მეტი მშრალი მატჩი."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "თავდამსხმელი", "record_type": "გატანილი გოლები",
             "player": "დელიო ონი", "value": 299,
             "description": "საფრანგეთის ლიგა 1-ის ყველა დროის საუკეთესო ბომბარდირი."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "თავდამსხმელი", "record_type": "საგოლე გადაცემა",
             "player": "დიმიტრი პაიე", "value": 100,
             "description": "ლიგა 1-ის რეკორდი საგოლე გადაცემებისთვის თავდამსხმელისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "თავდამსხმელი", "record_type": "ყვითელი ბარათი",
             "player": "სტეფან ლიხტშტაინერი", "value": 80,
             "description": "ლიგა 1-ის რეკორდი ყვითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "თავდამსხმელი", "record_type": "წითელი ბარათი",
             "player": "ედინსონ კავანი", "value": 3,
             "description": "ლიგა 1-ის რეკორდი წითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "ნახევარმცველი", "record_type": "გატანილი გოლები",
             "player": "ბერნარ ლამბურდი", "value": 135,
             "description": "ლიგა 1-ის რეკორდი გატანილი გოლებისთვის ნახევარმცველისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "ნახევარმცველი", "record_type": "საგოლე გადაცემა",
             "player": "ჟერომ როტენი", "value": 90,
             "description": "ლიგა 1-ის რეკორდი საგოლე გადაცემებისთვის ნახევარმცველისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "ნახევარმცველი", "record_type": "ყვითელი ბარათი",
             "player": "მატიე ბოდმერი", "value": 95,
             "description": "ლიგა 1-ის რეკორდი ყვითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "ნახევარმცველი", "record_type": "წითელი ბარათი",
             "player": "ტიაგო მოტა", "value": 10,
             "description": "ლიგა 1-ის რეკორდი წითელი ბარათებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მცველი", "record_type": "გატანილი გოლები",
             "player": "ჟან-პიერ ადამსი", "value": 40,
             "description": "ლიგა 1-ის რეკორდი გატანილი გოლებისთვის მცველის პოზიციაზე."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მცველი", "record_type": "საგოლე გადაცემა",
             "player": "მატიე დებიში", "value": 30,
             "description": "ლიგა 1-ის რეკორდი საგოლე გადაცემებისთვის მცველის პოზიციაზე."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მცველი", "record_type": "მშრალი კარი",
             "player": "ტიაგო სილვა", "value": 110,
             "description": "ლიგა 1-ის რეკორდი მშრალი კარისთვის მცველის პოზიციაზე (გუნდური მშრალი თამაშები)."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მცველი", "record_type": "ყვითელი ბარათი",
             "player": "ანტუან კონტი", "value": 85,
             "description": "ლიგა 1-ის რეკორდი ყვითელი ბარათებისთვის მცველისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მცველი", "record_type": "წითელი ბარათი",
             "player": "სტივ მენდანდა", "value": 6,
             "description": "ლიგა 1-ის რეკორდი წითელი ბარათებისთვის მცველისთვის."},
            {"championship": "საფრანგეთის ლიგა 1", "position": "მეკარე", "record_type": "მშრალი კარი",
             "player": "მიკაელ ლანდრო", "value": 150,
             "description": "ლიგა 1-ის რეკორდი მშრალი მატჩებისთვის მეკარისთვის."},
            {"championship": "ჩემპიონთა ლიგა", "position": "თავდამსხმელი", "record_type": "გატანილი გოლები",
             "player": "კრიშტიანუ რონალდუ", "value": 140,
             "description": "ჩემპიონთა ლიგის ყველა დროის საუკეთესო ბომბარდირი."},
            {"championship": "ჩემპიონთა ლიგა", "position": "თავდამსხმელი", "record_type": "საგოლე გადაცემა",
             "player": "კრიშტიანუ რონალდუ", "value": 42,
             "description": "ჩემპიონთა ლიგის ყველა დროის საუკეთესო ასისტენტი."},
            {"championship": "ჩემპიონთა ლიგა", "position": "თავდამსხმელი", "record_type": "ყვითელი ბარათი",
             "player": "რაფაელ ვარანი", "value": 38,
             "description": "ჩემპიონთა ლიგის რეკორდი ყვითელი ბარათებისთვის თავდამსხმელისთვის (პირობითი)."},
            {"championship": "ჩემპიონთა ლიგა", "position": "თავდამსხმელი", "record_type": "წითელი ბარათი",
             "player": "ზლატან იბრაჰიმოვიჩი", "value": 4,
             "description": "ჩემპიონთა ლიგის რეკორდი წითელი ბარათებისთვის თავდამსხმელისთვის."},
            {"championship": "ჩემპიონთა ლიგა", "position": "ნახევარმცველი", "record_type": "გატანილი გოლები",
             "player": "ფრენკ ლემპარდი", "value": 23,
             "description": "ჩემპიონთა ლიგის რეკორდი გატანილი გოლებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "ჩემპიონთა ლიგა", "position": "ნახევარმცველი", "record_type": "საგოლე გადაცემა",
             "player": "ლიონელ მესი", "value": 40,
             "description": "ჩემპიონთა ლიგის რეკორდი საგოლე გადაცემებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "ჩემპიონთა ლიგა", "position": "ნახევარმცველი", "record_type": "ყვითელი ბარათი",
             "player": "პოლ სქოულზი", "value": 45,
             "description": "ჩემპიონთა ლიგის რეკორდი ყვითელი ბარათებისთვის ნახევარმცველისთვის."},
            {"championship": "ჩემპიონთა ლიგა", "position": "ნახევარმცველი", "record_type": "წითელი ბარათი",
             "player": "პოლ სქოულზი", "value": 4,
             "description": "ჩემპიონთა ლიგის რეკორდი წითელი ბარათებისთვის ნახევარმცველის პოზიციაზე."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მცველი", "record_type": "გატანილი გოლები",
             "player": "სერხიო რამოსი", "value": 15,
             "description": "ჩემპიონთა ლიგის რეკორდი გატანილი გოლებისთვის მცველის პოზიციაზე."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მცველი", "record_type": "საგოლე გადაცემა",
             "player": "მარსელო", "value": 23,
             "description": "ჩემპიონთა ლიგის რეკორდი საგოლე გადაცემებისთვის მცველის პოზიციაზე."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მცველი", "record_type": "მშრალი კარი",
             "player": "პაოლო მალდინი", "value": 100,
             "description": "ჩემპიონთა ლიგის რეკორდი მშრალი კარისთვის მცველის პოზიციაზე (გუნდური მშრალი თამაშები)."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მცველი", "record_type": "ყვითელი ბარათი",
             "player": "სერხიო რამოსი", "value": 38,
             "description": "ჩემპიონთა ლიგის რეკორდი ყვითელი ბარათებისთვის მცველისთვის."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მცველი", "record_type": "წითელი ბარათი",
             "player": "სერხიო რამოსი", "value": 4,
             "description": "ჩემპიონთა ლიგის რეკორდი წითელი ბარათებისთვის მცველისთვის."},
            {"championship": "ჩემპიონთა ლიგა", "position": "მეკარე", "record_type": "მშრალი კარი",
             "player": "იკერ კასილასი", "value": 57,
             "description": "ჩემპიონთა ლიგის რეკორდი მშრალი მატჩებისთვის მეკარისთვის."},
        ]

        self.position_record_available = {
            "თავდამსხმელი": ["გატანილი გოლები", "საგოლე გადაცემა", "ყვითელი ბარათი", "წითელი ბარათი"],
            "ნახევარმცველი": ["გატანილი გოლები", "საგოლე გადაცემა", "ყვითელი ბარათი", "წითელი ბარათი"],
            "მცველი": ["გატანილი გოლები", "საგოლე გადაცემა", "მშრალი კარი", "ყვითელი ბარათი", "წითელი ბარათი"],
            "მეკარე": ["მშრალი კარი"],
        }
        self.ui.showRecordButton.clicked.connect(self.display_record)
        self.ui.championshipComboBox.currentIndexChanged.connect(self.reset_display_on_change)
        self.ui.positionComboBox.currentIndexChanged.connect(self.update_record_type_combobox)
        self.ui.recordTypeComboBox.currentIndexChanged.connect(self.reset_display_on_change)

        self.update_record_type_combobox()

    def reset_display_on_change(self):
        self.ui.recordDisplayLabel.setText("აირჩიეთ კრიტერიუმები და დააჭირეთ 'რეკორდის ჩვენებას'.")
        self.ui.recordDescriptionLabel.setText("")
        self.ui.statusbar.showMessage("განაახლეთ არჩევანი და დააჭირეთ ღილაკს.", 3000)

    def update_record_type_combobox(self):
        selected_position = self.ui.positionComboBox.currentText()
        available_record_types = self.position_record_available.get(selected_position, [])
        self.ui.recordTypeComboBox.clear()
        if available_record_types:
            self.ui.recordTypeComboBox.addItems(available_record_types)
            self.ui.recordTypeComboBox.setEnabled(True)
        else:
            self.ui.recordTypeComboBox.setEnabled(False)
        self.reset_display_on_change()

    def display_record(self):
        selected_championship = self.ui.championshipComboBox.currentText()
        selected_position = self.ui.positionComboBox.currentText()
        selected_record_type = self.ui.recordTypeComboBox.currentText()

        if not selected_championship or not selected_position or not selected_record_type:
            self.ui.recordDisplayLabel.setText("გთხოვთ, აირჩიეთ ყველა კრიტერიუმი.")
            self.ui.recordDescriptionLabel.setText("")
            self.ui.statusbar.showMessage("აირჩიეთ ყველა კრიტერიუმი.", 3000)
            return

        filtered_records = []
        for record in self.football_records:
            match_championship = (record["championship"] == selected_championship)
            match_position = (record["position"] == selected_position)
            match_record_type = (record["record_type"] == selected_record_type)

            if match_championship and match_position and match_record_type:
                filtered_records.append(record)

        if filtered_records:
            record_to_display = filtered_records[0]

            ending_text = ""
            if record_to_display['record_type'] == "გატანილი გოლები":
                ending_text = "გოლი"
            elif record_to_display['record_type'] == "საგოლე გადაცემა":
                ending_text = "გადაცემა"
            elif record_to_display['record_type'] == "მშრალი კარი":
                ending_text = "მშრალი კარი"
            elif record_to_display['record_type'] == "ყვითელი ბარათი":
                ending_text = "ყვითელი ბარათი"
            elif record_to_display['record_type'] == "წითელი ბარათი":
                ending_text = "წითელი ბარათი"
            else:
                ending_text = record_to_display['record_type'].lower()

            record_text = (
                f"{record_to_display['player']}: "
                f"{record_to_display['value']} {ending_text}"
            )

            self.ui.recordDisplayLabel.setText(record_text)
            self.ui.recordDescriptionLabel.setText(record_to_display['description'])
            self.ui.statusbar.showMessage("რეკორდი მოიძებნა!", 3000)
        else:
            self.ui.recordDisplayLabel.setText(
                "მოცემული კრიტერიუმებით რეკორდი არ მოიძებნა. (ეს არ უნდა მოხდეს, შეამოწმეთ ComboBox-ები!)")
            self.ui.recordDescriptionLabel.setText("გთხოვთ, დარწმუნდით, რომ ComboBox-ების მნიშვნელობები სწორია.")
            self.ui.statusbar.showMessage("რეკორდი ვერ მოიძებნა.", 3000)


app = QApplication(sys.argv)
window = FootballRecordsApp()
window.show()
sys.exit(app.exec_())