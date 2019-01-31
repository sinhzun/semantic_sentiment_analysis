import argparse

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, type=str, help="Original dataset file")
    args = parser.parse_args()
    return args

def preprocess(lines):
    sentences, aspects, labels = [], [], []
    for line in lines:
        if line.find('/n') != -1:
            labels.append('n')
            line_no_label = line.replace('/n', '')
            sentences.append(line_no_label)
        if line.find('/p') != -1:
            labels.append('p')
            line_no_label = line.replace('/p', '')
            sentences.append(line_no_label)
        if line.find('/0') != -1:
            labels.append('0')
            line_no_label = line.replace('/0', '')
            sentences.append(line_no_label)
        aspects.append([])
        for word in line.split():
            if word.endswith('/n'):
                word = word.replace('/n', '')
                aspects[len(aspects)-1].append(word)
            if word.endswith('/p'):
                word = word.replace('/p', '')
                aspects[len(aspects)-1].append(word)
            if word.endswith('/0'):
                word = word.replace('/0', '')
                aspects[len(aspects)-1].append(word)
    return sentences, aspects, labels

if __name__ == '__main__':
    args = create_arg_parser()
    input_file = args.f
    with open(input_file, 'rb') as f:
        lines = f.readlines()
    sentences, aspects, labels = preprocess(lines)
    with open(input_file + '.snt', 'wb') as fw:
        for sent in sentences:
            fw.write(sent)
    with open(input_file + '.apt', 'wb') as fw:
        for a in aspects:
            fw.write(str(a))
            fw.write('\n')
    with open(input_file + '.lbl', 'wb') as fw:
        for l in labels:
            fw.write(l)
            fw.write('\n')