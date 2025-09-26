import customtkinter as ctk
from customtkinter import filedialog
import os


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.geometry("510x900+0+0")
        self.title("Files Separator")
        
        #self.main_folder = ctk.StringVar()
        
        self.num_img = ctk.StringVar()
        self.num_video = ctk.StringVar()
        self.num_audio = ctk.StringVar()
        self.num_doc = ctk.StringVar()
        self.num_others = ctk.StringVar()
        
        
        self.app_label = ctk.CTkLabel(master=self, text="FILES SEPARATOR", font=("Arial", 30, "bold"), text_color="#FFFFFF", fg_color="#3B8ED0", corner_radius=10, height=50)
        self.app_label.pack(fill="x", padx=10, pady=(10,0))
    
        self.details_f = ctk.CTkFrame(master=self)
        self.details_f.pack(fill="both", expand=True, padx=10, pady=(10, 0))
        
        self.details_f.grid_rowconfigure(0, weight=1)
        self.details_f.grid_rowconfigure(7, weight=1)
        self.details_f.grid_columnconfigure(0, weight=2)
        self.details_f.grid_columnconfigure(1, weight=1)
        self.details_f.grid_columnconfigure(2, weight=1)
        self.details_f.grid_columnconfigure(3, weight=2)
        
        # Heading inside of the details frame
        info_label = ctk.CTkLabel(master=self.details_f, text="Number of files", font=("Arial", 17))
        info_label.grid(row=1, column=1, columnspan=2)
        
        # Image label
        img_label = ctk.CTkLabel(master=self.details_f, text="Image", font=("Arial", 17))
        img_label.grid(row=2, column=1, padx=60, pady=5)
        
        # Image Entry
        img_entry = ctk.CTkEntry(master=self.details_f, font=("Arial", 17), width=100, textvariable=self.num_img)
        img_entry.grid(row=2, column=2, padx=60, pady=5, ipady=2)
        
        # Audio label
        audio_label = ctk.CTkLabel(master=self.details_f, text="Audio", font=("Arial", 17))
        audio_label.grid(row=3, column=1, padx=60, pady=5)
        
        # Audio Entry
        audio_entry = ctk.CTkEntry(master=self.details_f, font=("Arial", 17), width=100, textvariable=self.num_audio)
        audio_entry.grid(row=3, column=2, padx=60, pady=5, ipady=2)
        
        # Video label
        video_label = ctk.CTkLabel(master=self.details_f, text="Video", font=("Arial", 17))
        video_label.grid(row=4, column=1, padx=60, pady=5)
        
        # Video Entry
        video_entry = ctk.CTkEntry(master=self.details_f, font=("Arial", 17), width=100, textvariable=self.num_video)
        video_entry.grid(row=4, column=2, padx=60, pady=5, ipady=2)
        
        # Documents label
        doc_label = ctk.CTkLabel(master=self.details_f, text="Documents", font=("Arial", 17))
        doc_label.grid(row=5, column=1, padx=60, pady=5)
        
        # Documents Entry
        doc_entry = ctk.CTkEntry(master=self.details_f, font=("Arial", 15), width=100, textvariable=self.num_doc)
        doc_entry.grid(row=5, column=2, padx=60, pady=5, ipady=2)
        
        # Others label
        others_label = ctk.CTkLabel(master=self.details_f, text="Others", font=("Arial", 17))
        others_label.grid(row=6, column=1, padx=60, pady=5)

        # Others Entry
        others_entry = ctk.CTkEntry(master=self.details_f, font=("Arial", 15), width=100, textvariable=self.num_others)
        others_entry.grid(row=6, column=2, padx=60, pady=5, ipady=2)

        # Main frame
        self.main_f = ctk.CTkFrame(master=self)
        self.main_f.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.main_f.grid_rowconfigure(0, weight=1)
        self.main_f.grid_rowconfigure(14, weight=1)
        self.main_f.grid_columnconfigure(0, weight=3)
        self.main_f.grid_columnconfigure(1, weight=1)
        self.main_f.grid_columnconfigure(2, weight=1)
        self.main_f.grid_columnconfigure(3, weight=3)
        
        # Main folder
        
        # Label
        self.main_label = ctk.CTkLabel(master=self.main_f, text="Select Main Folder", font=("Arial", 15))
        self.main_label.grid(row=1, column=1, padx=10, sticky="w")        
        
        # Path select entry
        self.main_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.main_entry.grid(row=2, column=1, padx=10, pady=10, ipady=2, sticky="we")
        
        # Path select button
        self.sm_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.sm_button.grid(row=2, column=2, padx=10, pady=10, ipady=2)

        # Image
        
        # Label
        self.img_label = ctk.CTkLabel(master=self.main_f, text="Select Image Folder", font=("Arial", 15))
        self.img_label.grid(row=3, column=1, sticky="w", padx=10)
        
        # Path select entry
        self.img_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.img_entry.grid(row=4, column=1, padx=10, pady=10, ipady=2, sticky="we")
        
        # Path select button
        self.si_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.si_button.grid(row=4, column=2, padx=10, pady=10, ipady=2)

        # Audio 
        
        # Label
        self.aud_label = ctk.CTkLabel(master=self.main_f, text="Select Audio Folder", font=("Arial", 15))
        self.aud_label.grid(row=5, column=1, sticky="w", padx=10)
        
        # Path select entry
        self.aud_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.aud_entry.grid(row=6, column=1, padx=10, pady=10, ipady=2, sticky="we")
        
        # Path select button
        self.sa_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.sa_button.grid(row=6, column=2, padx=10, pady=10, ipady=2)
        
        # Video
        
        # Label
        self.vid_label = ctk.CTkLabel(master=self.main_f, text="Select Video Folder", font=("Arial", 15))
        self.vid_label.grid(row=7, column=1, sticky="w", padx=10)
        
        # Path select entry
        self.vid_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.vid_entry.grid(row=8, column=1, padx=10, pady=10, ipady=2, sticky="we")
        
        # Path select button
        self.sv_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.sv_button.grid(row=8, column=2, padx=10, pady=10, ipady=2)

        # Documents
        
        # Label
        self.doc_label = ctk.CTkLabel(master=self.main_f, text="Select Documents Folder", font=("Arial", 15))
        self.doc_label.grid(row=9, column=1, sticky="w", padx=10) 
        
        # Path select entry
        self.doc_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.doc_entry.grid(row=10, column=1, padx=10, pady=10, ipady=2, sticky="we")
        
        # Path select button
        self.sd_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.sd_button.grid(row=10, column=2, padx=10, pady=10, ipady=2)
        
        # Others
        
        # Label
        self.oth_label = ctk.CTkLabel(master=self.main_f, text="Select Others Folder", font=("Arial", 15))
        self.oth_label.grid(row=11, column=1, sticky="w", padx=10)
        
        # Path select entry
        self.oth_entry = ctk.CTkEntry(master=self.main_f, font=("Arial", 15), width=350)
        self.oth_entry.grid(row=12, column=1, padx=10, pady=10, ipady=4, sticky="we")
        
        # Path select button
        self.so_button = ctk.CTkButton(master=self.main_f, text="Select Path", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=30, height=30)
        self.so_button.grid(row=12, column=2, padx=10, pady=10, ipady=4)
        
        # Move button
        self.move_button = ctk.CTkButton(master=self.main_f, text="Move", font=("Arial", 17), text_color="#FFFFFF", fg_color="#3B8ED0", width=100, height=35)
        self.move_button.grid(row=13, column=1, columnspan=2, padx=10, pady=10, ipady=2)
    
    # def browse_source(self):
    #     folder = filedialog.askdirectory()
    #     if folder:
    #         self.main_folder.delete(0, ctk.END)
    #         self.main_folder.insert(0, folder)

    # def num_files(self):
    #     image_ext = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heic", ".heif", ".svg", ".eps", ".ai")
    #     doc_ext = ('.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.md', '.html', '.xml', '.xls', '.xlsx', '.ppt', '.pptx')
    #     video_ext = ('.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm', '.3gp', '.mpeg', '.mpg')
    #     audio_ext = ('.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma', '.alac', '.aiff', '.opus')
        
    #     files = os.listdir(str(self.main_folder))

    #     num_images = []
    #     num_video = []
    #     num_audio = []
    #     num_doc = []
    #     num_others = []

    #     for file in files:
    #         file.lower().endswith(image_ext)
    #         num_images.append(file)
    #     for file in files:
    #         file.lower().endswith(video_ext)
    #         num_video.append(file)
    #     for file in files:
    #         file.lower().endswith(audio_ext)
    #         num_audio.append(file)
    #     for file in files:
    #         file.lower().endswith(doc_ext)
    #         num_doc.append(file)
        
    #     self.num_img.set(len(num_images))
    #     self.num_video.set(len(num_video))
    #     self.num_audio.set(len(num_audio))
    #     self.num_doc.set(len(num_doc))
    
    
if __name__ == "__main__":
    main_app = MainApplication()
    main_app.mainloop()
    
    