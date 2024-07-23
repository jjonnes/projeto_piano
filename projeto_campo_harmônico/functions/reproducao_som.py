import pygame
import os

class ReprodutorSom:
    def __init__(self):
        pygame.init()
        pygame.mixer.set_num_channels(12)  # Define o número máximo de canais de áudio

        self.dir_notas = os.path.join(os.path.dirname(__file__), 'notas')

        self.notas_sons = {
            "C3":  os.path.join(self.dir_notas, "GrandPianoLong_13_C3_78_SP.wav"),
            "C3#": os.path.join(self.dir_notas, "GrandPianoLong_14_C#3_78_SP.wav"),
            "D3":  os.path.join(self.dir_notas, "GrandPianoLong_15_D3_78_SP.wav"),
            "D3#": os.path.join(self.dir_notas, "GrandPianoLong_16_D#3_78_SP.wav"),
            "E3":  os.path.join(self.dir_notas, "GrandPianoLong_17_E3_78_SP.wav"),
            "F3":  os.path.join(self.dir_notas, "GrandPianoLong_18_F3_78_SP.wav"),
            "F3#": os.path.join(self.dir_notas, "GrandPianoLong_19_F#3_78_SP.wav"),
            "G3":  os.path.join(self.dir_notas, "GrandPianoLong_20_G3_78_SP.wav"),
            "G3#": os.path.join(self.dir_notas, "GrandPianoLong_21_G#3_78_SP.wav"),
            "A3":  os.path.join(self.dir_notas, "GrandPianoLong_22_A3_78_SP.wav"),
            "A3#": os.path.join(self.dir_notas, "GrandPianoLong_23_A#3_78_SP.wav"),
            "B3":  os.path.join(self.dir_notas, "GrandPianoLong_24_B3_78_SP.wav"),
            "C4":  os.path.join(self.dir_notas, "GrandPianoLong_25_C4_78_SP.wav"),
            "C4#": os.path.join(self.dir_notas, "GrandPianoLong_26_C#4_78_SP.wav"),
            "D4":  os.path.join(self.dir_notas, "GrandPianoLong_27_D4_78_SP.wav"),
            "D4#": os.path.join(self.dir_notas, "GrandPianoLong_28_D#4_78_SP.wav"),
            "E4":  os.path.join(self.dir_notas, "GrandPianoLong_29_E4_78_SP.wav"),
            "F4":  os.path.join(self.dir_notas, "GrandPianoLong_30_F4_78_SP.wav"),
            "F4#": os.path.join(self.dir_notas, "GrandPianoLong_31_F#4_78_SP.wav"),
            "G4":  os.path.join(self.dir_notas, "GrandPianoLong_32_G4_78_SP.wav"),
            "G4#": os.path.join(self.dir_notas, "GrandPianoLong_33_G#4_78_SP.wav"),
            "A4":  os.path.join(self.dir_notas, "GrandPianoLong_34_A4_78_SP.wav"),
            "A4#": os.path.join(self.dir_notas, "GrandPianoLong_35_A#4_78_SP.wav"),
            "B4":  os.path.join(self.dir_notas, "GrandPianoLong_36_B4_78_SP.wav"),
            "C5":  os.path.join(self.dir_notas, "GrandPianoLong_37_C5_78_SP.wav"),
            "C5#": os.path.join(self.dir_notas, "GrandPianoLong_38_C#5_78_SP.wav"),
            "D5":  os.path.join(self.dir_notas, "GrandPianoLong_39_D5_78_SP.wav"),
            "D5#": os.path.join(self.dir_notas, "GrandPianoLong_40_D#5_78_SP.wav"),
            "E5":  os.path.join(self.dir_notas, "GrandPianoLong_41_E5_78_SP.wav"),
            "F5":  os.path.join(self.dir_notas, "GrandPianoLong_42_F5_78_SP.wav"),
            "F5#": os.path.join(self.dir_notas, "GrandPianoLong_43_F#5_78_SP.wav"),
            "G5":  os.path.join(self.dir_notas, "GrandPianoLong_44_G5_78_SP.wav"),
            "G5#": os.path.join(self.dir_notas, "GrandPianoLong_45_G#5_78_SP.wav"),
            "A5":  os.path.join(self.dir_notas, "GrandPianoLong_46_A5_78_SP.wav"),
            "A5#": os.path.join(self.dir_notas, "GrandPianoLong_47_A#5_78_SP.wav"),
            "B5":  os.path.join(self.dir_notas, "GrandPianoLong_48_B5_78_SP.wav")
        }

        # Inicializa os canais de áudio para cada nota
        self.channels = {}
        for nota, arquivo in self.notas_sons.items():
            self.channels[nota] = pygame.mixer.Sound(arquivo)

    def tocar_nota(self, nota):
        try:
            # Toca a nota no canal correspondente
            self.channels[nota].play()
        except KeyError:
            print(f"Nota {nota} não encontrada.")
