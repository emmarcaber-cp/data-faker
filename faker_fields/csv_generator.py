class CSVGenerator:
    def __init__(self, fake, fields, types, num_rows, file_path, progress_callback=None):
        self.fake = fake
        self.fields = fields
        self.types = types
        self.num_rows = num_rows
        self.file_path = file_path
        self.progress_callback = progress_callback

    def generate(self):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
            import csv
            writer = csv.writer(csvfile)
            writer.writerow(self.fields)
            for i in range(self.num_rows):
                row = [t.generate(self.fake) for t in self.types]
                writer.writerow(row)
                if self.progress_callback and (i+1) % max(1, self.num_rows // 100) == 0:
                    percent = int(((i+1) / self.num_rows) * 100)
                    self.progress_callback(percent)
            if self.progress_callback:
                self.progress_callback(100)
