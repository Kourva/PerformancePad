#!/usr/bin/env python3

## Performance Pad GUI app Made in Python
## GITHUB: https://github.com/Kourva/PerformancePad

# Imports
from sys import exit
import pygame
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar.toolbar import MDTopAppBar
from kivymd.uix.slider.slider import MDSlider
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton
from kivy.clock import Clock
from kivymd.uix.progressbar.progressbar import MDProgressBar
from kivymd.uix.spinner.spinner import MDSpinner

# Mixer initialize
pygame.mixer.init()

# App Class
class PerformancePadApp(MDApp):

    # Opens Github Dialog
    def githubOpen(self, *args):
        self.Github.open()

    # Closes Github Dialog
    def githubClose(self, *args):
        self.Github.dismiss(force=True)

    # Update Kick
    def kick_update(self, *args):
        if self.Kick_mode == "inactive":
            self.Kick_mode = "active"
            self.Kick.text = "Activing..."
            self.Spinner.active = True
        else:
            self.Kick_mode = "inactive"
            self.Kick.text = "Inactiving..."
            self.Spinner.active = True

    # Update HiHat
    def hihat_update(self, *args):
        if self.HiHat_mode == "inactive":
            self.HiHat_mode = "active"
            self.HiHat.text = "Activing..."
            self.Spinner.active = True
        else:
            self.HiHat_mode = "inactive"
            self.HiHat.text = "Inactiving..."
            self.Spinner.active = True

    # Update Clap
    def clap_update(self, *args):
        if self.Clap_mode == "inactive":
            self.Clap_mode = "active"
            self.Clap.text = "Activing..."
            self.Spinner.active = True
        else:
            self.Clap_mode = "inactive"
            self.Clap.text = "Inactiving..."
            self.Spinner.active = True

    # Update Piano
    def piano_update(self, *args):
        if self.Piano_mode == "inactive":
            self.Piano_mode = "active"
            self.Piano.text = "Activing..."
            self.Spinner.active = True
        else:
            self.Piano_mode = "inactive"
            self.Piano.text = "Inactiving..."
            self.Spinner.active = True

    # Update Harp
    def harp_update(self, *args):
        if self.Harp_mode == "inactive":
            self.Harp_mode = "active"
            self.Harp.text = "Activing..."
            self.Spinner.active = True
        else:
            self.Harp_mode = "inactive"
            self.Harp.text = "Inactiving..."
            self.Spinner.active = True

    # Update BGuitar
    def bguitar_update(self, *args):
        if self.BGuitar_mode == "inactive":
            self.BGuitar_mode = "active"  
            self.BGuitar.text = "Activing..."
            self.Spinner.active = True
        else:
            self.BGuitar_mode = "inactive"
            self.BGuitar.text = "Inactiving..."
            self.Spinner.active = True

    # Updater
    def update(self, *args):
        self.Spinner.active = False
        # Kick
        if self.Kick_mode == "active":
            self.Kick.md_bg_color = "purple"
            kick_channel = pygame.mixer.Channel(0)
            kick_loop = pygame.mixer.Sound("Loops/kick.wav")
            kick_channel.play(kick_loop)
            self.Kick.text = "Kick"
        else:
            self.Kick.md_bg_color = "gray"
            self.Kick.text = "Kick"

        # HiHat
        if self.HiHat_mode == "active":
            self.HiHat.md_bg_color = "purple"
            hihat_channel = pygame.mixer.Channel(1)
            hihat_loop = pygame.mixer.Sound("Loops/hihat.wav")
            hihat_channel.play(hihat_loop)
            self.HiHat.text = "HiHat"
        else:
            self.HiHat.md_bg_color = "gray"
            self.HiHat.text = "HiHat"

        # Clap
        if self.Clap_mode == "active":
            self.Clap.md_bg_color = "purple"
            clap_channel = pygame.mixer.Channel(2)
            clap_loop = pygame.mixer.Sound("Loops/clap.wav")
            clap_channel.play(clap_loop)
            self.Clap.text = "Clap"
        else:
            self.Clap.md_bg_color = "gray"
            self.Clap.text = "Clap"

        # Piano
        if self.Piano_mode == "active":
            self.Piano.md_bg_color = "purple"
            piano_channel = pygame.mixer.Channel(3)
            piano_loop = pygame.mixer.Sound("Loops/piano.wav")
            piano_channel.play(piano_loop)
            self.Piano.text = "Piano"
        else:
            self.Piano.md_bg_color = "gray"
            self.Piano.text = "Piano"

        # Harp
        if self.Harp_mode == "active":
            self.Harp.md_bg_color = "purple"
            harp_channel = pygame.mixer.Channel(4)
            harp_loop = pygame.mixer.Sound("Loops/harp.wav")
            harp_channel.play(harp_loop)
            self.Harp.text = "Harp"
        else:
            self.Harp.md_bg_color = "gray"
            self.Harp.text = "Harp"

        # BGuitar
        if self.BGuitar_mode == "active":
            self.BGuitar.md_bg_color = "purple"
            bguitar_channel = pygame.mixer.Channel(5)
            bguitar_loop = pygame.mixer.Sound("Loops/bguitar.wav")
            bguitar_channel.play(bguitar_loop)
            self.BGuitar.text = "Bass Guitar"
        else:
            self.BGuitar.md_bg_color = "gray"
            self.BGuitar.text = "Bass Guitar"

    def PBupdate(self, *args):
        if self.ProgressBar.value == 100:
            self.ProgressBar.value = 12.5
        elif self.ProgressBar.value == 12.5:
            self.ProgressBar.value = 25
        elif self.ProgressBar.value == 25:
            self.ProgressBar.value = 37.5
        elif self.ProgressBar.value == 37.5:
            self.ProgressBar.value = 50
        elif self.ProgressBar.value == 50:
            self.ProgressBar.value = 62.5
        elif self.ProgressBar.value == 62.5:
            self.ProgressBar.value = 75
        elif self.ProgressBar.value == 75:
            self.ProgressBar.value = 87.5
        elif self.ProgressBar.value == 87.5:
            self.ProgressBar.value = 100

    # Build method
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        # Active
        self.Kick_mode = "inactive"
        self.HiHat_mode = "inactive"
        self.Clap_mode = "inactive"
        self.Piano_mode = "inactive"
        self.Harp_mode = "inactive"
        self.BGuitar_mode = "inactive"

        # Home Screen
        home = MDScreen()

        # Top Toolbar
        self.Toolbar = MDTopAppBar(
            title = "Performance Pad",
            pos_hint = {"top": 1},
            right_action_items = [
                ["github", self.githubOpen],
                ["close-thick", lambda _: exit()]
            ]
        )

        # Github Dialog
        self.Github = MDDialog(
            title = "Developer",
            text = "Github: https://github.com/Kourva",
            buttons = [
                MDFlatButton(
                    text = "Close",
                    theme_text_color = "Custom",
                    text_color = "white",
                    on_press = self.githubClose
                )
            ]
        )

        # Kick Botton
        self.Kick = MDRaisedButton(
            text = "Kick",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.25, "center_y": 0.75},
            on_press = self.kick_update
        )

        # HiHat Botton
        self.HiHat = MDRaisedButton(
            text = "HiHat",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.5, "center_y": 0.75},
            on_press = self.hihat_update
        )

        # Clap
        self.Clap = MDRaisedButton(
            text = "Clap",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.75, "center_y": 0.75},
            on_press = self.clap_update
        )

        # Piano
        self.Piano = MDRaisedButton(
            text = "Piano",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.25, "center_y": 0.55},
            on_press = self.piano_update
        )

        # Harp 
        self.Harp = MDRaisedButton(
            text = "Harp",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.5, "center_y": 0.55},
            on_press = self.harp_update
        )

        # BGuitar
        self.BGuitar = MDRaisedButton(
            text = "Bass Guitar",
            font_size = 20,
            size_hint=(.2, .15),
            md_bg_color = "gray",
            pos_hint = {"center_x": 0.75, "center_y": 0.55},
            on_press = self.bguitar_update
        )

        # ProgressBar
        self.ProgressBar = MDProgressBar(
            value = 12.5,
            size_hint=(.55, None),
            pos_hint = {"center_x": 0.5, "center_y": 0.25},
        )

        # PB Text
        self.PBText = MDLabel(
            text = "Beat Step",
            font_size = 20,
            halign = "center",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y": 0.30},
        )

        # ProgressBar Icons
        self.LIcon = MDIconButton(
            icon="numeric-0-box",
            pos_hint={"center_x": 0.18, "center_y": 0.25},
        )
        self.RIcon = MDIconButton(
            icon="numeric-8-box",
            pos_hint={"center_x": 0.82, "center_y": 0.25},
        )

        # Spinner
        self.Spinner = MDSpinner(
            size_hint = (None,None),
            size = (40,40),
            pos_hint = {'center_x': .5, 'center_y': .15},
            determinate = False
        )

        # Add widgets
        home.add_widget(self.Toolbar)
        home.add_widget(self.Kick)
        home.add_widget(self.HiHat)
        home.add_widget(self.Clap)
        home.add_widget(self.Piano)
        home.add_widget(self.Harp)
        home.add_widget(self.BGuitar)
        home.add_widget(self.PBText)
        home.add_widget(self.LIcon)
        home.add_widget(self.RIcon)
        home.add_widget(self.Spinner)
        home.add_widget(self.ProgressBar)

        # Updaters
        self.Spinner.active = False
        Clock.schedule_interval(lambda _:self.PBupdate(self), 1)
        Clock.schedule_interval(lambda _:self.update(self), 8)
        
        # Return home
        return home

# Run
PerformancePadApp().run()
