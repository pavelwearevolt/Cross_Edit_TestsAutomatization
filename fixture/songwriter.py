__author__ = 'Pavel Kosicin'
import time


class SongwriterHelper:

    def __init__(self, app):
        self.app = app

    def create_from_song(self, songwriter):
        wd = self.app.wd
        # open tab songwriter
        wd.find_element_by_link_text("Songwriters").click()
        # create songwriter
        wd.find_element_by_id("writing_new_search").click()
        wd.find_element_by_id("writing_new_search").clear()
        wd.find_element_by_id("writing_new_search").send_keys(songwriter.name)
        wd.find_element_by_id("writing_new_create").click()
        wd.find_element_by_link_text(songwriter.name).click()
        # fill identifications
        self.fill_fields(songwriter)
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # find created songwriter, open songwriter edit page
        self.app.navigate.menu_people()
        self.app.search.object_search(name="sw_#1")
        # add notes
        self.add_notes(songwriter)

    def create_menu_global_search(self, songwriter):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # create songwriter
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(songwriter.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='NTialWg8eHGF9sNIWyhYH']//button[.='person']").click()
        # select person type
        self.type()
        # find created songwriter
        self.app.navigate.menu_people()
        self.app.search.object_search(name="sw_#2")
        # fill fields on the songwriter edit page
        self.fill_fields(songwriter)
        # add notes
        self.add_notes(songwriter)

    def create_menu_people(self, songwriter):
        wd = self.app.wd
        # navigate menu people
        self.app.navigate.menu_people()
        # create songwriter
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(songwriter.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # select person type
        self.type()
        # find created songwriter
        self.app.navigate.menu_global_search()
        self.app.search.global_search(name="sw_#3")
        # fill fields on the songwriter edit page
        self.fill_fields(songwriter)
        # add notes
        self.add_notes(songwriter)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)

    def fill_fields(self, songwriter):
        wd = self.app.wd
        wd.find_element_by_id("songwriter_ipicae_identification_new").click()
        wd.find_element_by_id("songwriter_ipicae_identification_new").clear()
        wd.find_element_by_id("songwriter_ipicae_identification_new").send_keys(songwriter.ipipcae)
        wd.find_element_by_id("songwriter_ipicae_identification_new_add").click()
        wd.find_element_by_id("songwriter_asap_identification_new").click()
        wd.find_element_by_id("songwriter_asap_identification_new").clear()
        wd.find_element_by_id("songwriter_asap_identification_new").send_keys(songwriter.asap)
        wd.find_element_by_id("songwriter_asap_identification_new_add").click()

    def add_notes(self, songwriter):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").clear()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").send_keys(songwriter.note)
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/button").click()
        time.sleep(3)
