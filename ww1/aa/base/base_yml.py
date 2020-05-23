import yaml
def yml_data_with_file(filename):
    with open('./ww1/aa/data/'+ filename +'.yml','r') as f:
        a=yaml.load(f,Loader=yaml.FullLoader)
        print(a)
        return a


