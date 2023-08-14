from functionModule import *
# load the tokenizer
def PredictPic(imgname):
    filename = 'Flickr_8k.trainImages.txt'
    train = load_set(filename)
    train_descriptions = load_clean_descriptions('descriptions.txt', train)
    tokenizer = load(open('tokenizer.pkl', 'rb'))
    # pre-define the max sequence length (from training)
    max_length = 34
    # load the model
    model = load_model('model_18.h5')
    # load and prepare the photograph
    photo = extract_features(imgname)
    print(photo[0])
    tokenizer = create_tokenizer(train_descriptions)
    # generate description
    description = generate_desc(model, tokenizer, photo, max_length)
    return  description
    #print(description)
