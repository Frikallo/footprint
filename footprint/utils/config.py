import os

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.read_config()

    def write_config(self, config_file, config):
        print(f'Config file {config_file} not found, creating new one...')
        with open(config_file, 'w') as f:
            for key, value in config.items():
                f.write(f'{key}={value}')
        print('Done. Config saved at ' + os.path.abspath(config_file) + '\n')

    def read_config(self):
        config = {}
        try:
            with open(self.config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line == '':
                        continue
                    key, value = line.split('=', 1)
                    config[key] = value
        except FileNotFoundError:
            self.write_config(self.config_file, config)
        return config

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as f:
            for key, value in self.config.items():
                f.write(f'{key}={value}\n')
    
if __name__ == '__main__':
    config = Config('.conf')
    config.set('test', 'test')
    config.save()
    print(config.get('test'))