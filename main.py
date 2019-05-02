from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SearchForm
import sqlite3
import subprocess
import os
import sys
import re

app = Flask(__name__)

app.config['SECRET_KEY']='d780dc767f4cd0d8d9b92447b2f32e2d66c93e4ad9935b71a840ed4cbea9bc595daf8c967304717483f1f28e1b369928df9e5788d80cf5f1feddcd82052807e7495c7b15a7aa43e47b9d62a6c5834c8b66196daf511911bf5aa36d1100f47e4fcff35b3b86e96ebb4f6f602b1fe1220c3944de73c467104115ee6a6ab7466858efb89d136dd4e08e984893be7287005d573351dafcd2ed2ea177f7fcb74d45a8790dbb509094151e79e03f9b43659fd8e54389805f1d11e7788c6aa452eaa223793a9882a50d5a12e40fdcca4ff01add652f5388b2130b2e90135f7b005b1b5f8f61e0996d6d94c4c3429e23f6108460a1a3a8aeacd024570b58f02c529da945a145ccba3ed26b129fdda45ea07cc0336348b9d83ee3ac45420ae7a2b67b3ca3ef58a238de974ce3ab57c878bd9042dee9bddf94aa5b86e3c77f7cd1086b2afe4264efe4777b4167277054fca6d915579a22d863254ff52b99a50563628811771110172b235bdf070d5439759fc9ab35a3f224b19fad967679e00781367bb540cedc30406732ed1b417045186b830ddaa22d916c753981c106fc1f189966999a123547366217ff5b22df1bc207424a2b0726e2ae47e1a7fe32edb65b35d6da1b775f9ba687979e77d0147cc48d938e164dd659046ae8c85c58ceb086db2fde088ed345ce6f6ddcf39f347049ff474468acab3fa330d2d498c86f32a3933da6e538a06c376f0bd61dbb0f756b9c903ffd4eb77712dd10f39b531376f44e48606e6eba8ca6e4129d2f951bd780761fd962c912e8fe8475022c62ae665b9d0259825b54b73933875ed8682a68391d38f4fa26fc96bb0e3a86939e01abd65f4b7b7eb1c779bc3d627a5162b3540cade259fc0d4609793ce6bbc105f4802b8eeeb39bda025360ba9b23c604745d29537106bc1bffd625f0479bfe4e31de64aae3c2ce81ba6e236ce7fdd57819193272c300d2a26d4b6136aabc9e7d31ce3cba51b970ca51f7f76520ae57f2e29c01bc4a7254c4e083564e095781e45570f49ce85de4ddb1ec4940bd5191ce94b9155c4cd7d4490137656410291fc6a259f5698ab3890f0519b4e07edd8a7ba8fc265dd457e7dd542f4545889c35197d461c199802273840767c20cdfd724d564f08eaa8ca30f03e771553ce21657aec478a01c9332b387c993a0fe4acaa99a38095d52f989db2aa1c75fdb31b012028228605badfbf25a86fb05ecf69e37ff1d6ed5cfbac80faac7e2e0810f392ceacbab4bf1c325135c02e95a436156ae7054d450e351f30af0eb87091657bb8844deb9f899e470d8bfd1e7e298e161ca87ab223df8909f7107f76ad473e1fbda47b8e84ebf9d10b46c4735350df3641c8945728f49e9e30c774738dbf6143fabd7e5c0f256163fc7076e48a0ae0790c1f20da40877b02795f462882efd6c486da283da3238dd2c91476ea09586f07f73ad30c653a8444cc1f7fd6957421f868e34ece07c3a9b8de72b49deb663404b3cd93f08a7c70f837d962fcb1e03738819611e034c1edd8bbb982206f25b5cf073e2e4cffa8b0f09aca2c3cee70bb78eeea74a5170ce2312da6f28732ed0edecf58ae878f17eebe113a4363a82c64ac9d99434020ac725912b98ed99d141b4262095b1dcb29ed6806ae4d35ff204beb99a18f3652e1a81d760b54932317512ee0735c59fa82cb69e595d5f117b0cd0af8525d2ac5866c172976565ec981c3706fe3fe2199219e8f6c5b51381ad0ad69b4993be024562f8fc1532bc5ffbbec24007cd5e90927e3ddcfbeea4e257b66d36dd5535d72f3defb5584a100a9aa086184921b8b964ae17f4efa3273ea090bde247ef7ae4fa70a06e939b2fd59430471ffde0140752b069dc15103392033dad107e7f446d006217d11d6ce8a5dff1bcd325439f729570539d28eba47d534ec6e129ae11fe1c3fa5b64534984a31c00c96c6f3e5ac69614c0a069f6c11b07838b4b8da6dda4080b3b2800b93bd7eb06c45111601d26bd2ee292e2f5528102fbcdb21d5228c1ecfab477f5729eaeb432d631077f5b7ba81b0d56cabd4227fed958d2290a123cafb87dd39bcb8106ec76464389b601436b5d2225335eba0d145a4ec866384caadbcf0d9e961163340fe0de2491a8644674fa65bcf3b32fd0e72888cc97ed40e49ecdeaccbe1a647f609f89f28c0a9771bf4db8188ce454ff04855baded963c279cbbc95fdc14aea4ba28e6d23abbb42ae5123a0af10229dfca6ee9efb33816fd4faf3a01a206352d012b8d9f5eb560b4e9fdb4f1a2067f2da0fb5e9ad8e0c421247b765818b3de7b90332f6b7cd66547c6f213c553d7a15c72bad693f380427e055004325e738effad837601fc3745896d5950d52057a4f8a9869b2c7bda13edb38ce2a057ff587e2d11c34ea4ece3a932a3fe7d85270ebb2a4a804253494d1193c98700ab80c5f766f1be0b10ef51977d02949a23c1b2214c6c1607536a3ad4c607f91ef8b1376e89400ebc06c5607afe10f1f6fb56a958827dc0ef270fa0b08f597a1c63351179d575d08df29d162247ccb31dfbfe4b10647223831087d1555cb0c86a172606be6eea975bd0fc4e1f33eccf431a0fd80df1d96c2d8ff6f703798725945fd6ddcc48efbce5936c8bfcc1247624f69b9b58c3df36b0116a15e12549134bb03630412bf7a2565b947931b5b3a1191feaba6e45df59ae6b07b7fdea1fce92ef4394ddef3d5b8294e39ea375c9cd46676f47c8bd3dca4bd4fe8e91ed49cf41faa247f367a1bd31077640efd7c489ab49624e96fd4625efc2e705dc9f0ab2a3672cd5eeedd4d5c768deefcbe0cb9f22d2a3450f48d5a1b195d00b7459b72dd5fc720e1451ee1e6f9d1608ef51c590b4da6b2a3d586caa8d92bf1191a3e6cd8acbf9edde831c257d4f0ed1de3d0d59f543eac481a4d42796526e78d70293bc624297bd88bd70e8053261e44ac5be29ca438c2098d8a679858552f97c48344cce9f99c5f473db19a08b8bfe24112e171cc8dde56670d531f20f9a3bb39a39a0cb9d43e51cd153253397a9ccc683a6b187f29f534d6693ee9bf100e24bced76bfaadae2b7059bf542c5c34802503b48292f3eb6d8497e7f852e2cee20e34363e6c02fae83d93135d8fcadf6f861dd5f447e79e5fc160e15c5ff8e87058b8cb7321d7e789f179498970902455354802387b5f56e54e5109cca4df888150a52a22825a8ac758fe64f96ff0f59682a0e76e47a64b24d2ccde5e1c41575bad67b18055ce1d4d6c60c35256f5ebd88f6e22e12138f1834c1263c57aa42b92fe1fa12a9d620dd5b2e8f2976a235a8af252219c824b13e119314a66490ee7c4e0ddd0a827059aec4ae6661c796f2c7fe129f7d1ccc680badfe04f701f0d696b2974854ef36186b5ec116518283540506338402be041ff748cac60dac6b27ef60e8b74557d0e5a18552813296048f36ca704eed4572188d104470650caec1d430bc7c4a8398f59529496948393f3083610929de81e79333d5a5df5ec32e7cc971d850ee0da20bfed2740fed49950d234a8f0f9e0e61b7a54f422ea4e012d2fe22d46bccb6628b5f8448ea8e87a63e4ee12a57b8e3cb2416aecb81c9f60f80bf44e37986ead11cb17b037334dc29d598f7626c4c9520fc4c4ffef958b24ef0b401330b96e614a0d80686317525bc106e46a17428e7d8647ebf35ed320c1223213b81a5b5f7acc7c296e4b680ef547c4d8263576b86cf63e54b69e179ee6995b064aeaf590ed70db0e562a2736cd1f7eb5578d6ba04ff94b73273d0bee7403f90d0953f3b9fc9354fb0679dfb20a18238c90e18b937c0884c6054ab4bdc2627ef2e56b96d4ba6ddd1f54a15eb725c4d6829c87a299780f630c70c359a506ae76f8f1acabbd535f9d7e5cb852f4d90cdad9ddd326328ea30d3d6add0443afc15fc865bd873bce9e70d675b097283cf1694c868133b3ec2c0d6bf28eef1286561d2fc5a21dff3d57d3aa477ad209cb450da1f5aec1fe60a390ca4e30ea0702aa85f8a2f04888d51cf83691262e1a6d7a75c173c1df8b1e10672c22acb3e3487d57c5acd8a527278ee54048c4f71882bfda9f89bd3bbab25c9acd35d55ab4464840c8fc6bc40712f9a8547b3722efb6d0952780e304e31464b8e554dc4dae3ec5873dce36b0183146b76debefe49e5db4fe18ae1aa150294e24d658e51154c7aba2dfaf6c75d7fda00c3626a6f5adaf15e89b4066f41640dc1c9f4c75a08f43affc5449869349fdce708d87d957002f3782d6d29f6f02ee4492f0c9aa43b51287e2563f5fe08ef753cb0b0b634ccb45b0a8ba6d3f8fd88ce75bb1b6f80dffe5d28c937ca5eafb5b73b29b7edba3e95990e7f1e24d38f8f4820879966b26934ebe915eae35ec98113f5d04f1df51322bfeb17d151b5f2b7d66fd2eb2c1b37e8dc1aabc8aace9f50970e64e2934a958f6f77167954bf461258097bb1d62f701dd9183e45e9146e1a005271c20e6c2203ffb75feae6b42c5863b7d2ac4730e6b6fe58d1fe59ba706a6b8f4b040d6051825a744a0e15b6736754933e133403acd550ef9011279841b9ec9cd734b7dc117a463595ee868927cda0ce9bd49e59794976369f2b2cb03145febf1afa53a749ac6a50dc401243dfdde6faf5f06400475225111a7f74757834fa2df51887859c692af89f94b7716458ea29b29e6992fda4831a658f1fd8ca0ab2bbb8ad5984ad129f786b5fdcc13fbeaedbfcbf3971f07667a11a830aa86f98f5d0b371d04c295f2738e8222616c92e604ece7d05afe0c280b9b1822b9cd7d71c01252fef5007cefcc8672e55e1742c1fea097f5e8f318593959fd8a2591d3cc11a065df0e45236813706972838577e0d46006fa194e30cb5666f0ca8d43b90183d0aebc02096d12739b0d813f5d3431fcba028d1efc4fc8c1cf89f7a550c5fbc038619549ac81662185f9dfdb8cd9e04ff0ce5276d4fc90310882d0d3ccac37fcd136dc7d5ddb71fd85234f614f1a7982dd0432e4d29bf0ede144f87795379b789dd4fe52619fc9d5afc89d5423fed1884a04be80ad04dd9509618e032bbefd7fd6fb66339ba7f71bea6fc81a0ab966b29d9ab001c381ee56e49a85b38318ad26208c2343794194ba90ff249501cd3327a5340e9bdba740016783c7e5aff73ad1cf1d0c259d32a9fda8583164427494d5cc74a09c43e93798426352ed7e557491dfac46fc6da2dbe37883c2041f3e4e5c20a4268f0d9ba68be4bd77c79a396b2c66c7e8f7baf306457bc2852db8ebd278e7833fa81c9f064ffb86004dbe8fbccb9a8298af0373917608719432e001f3957082e51b0a20b4339e3ca336c2a774ced1f223bbaa26973f97575d3763340fccd5435048172120a3beeb1f684e49d393f1aa5c5811d7ff1960b2583f3402acaffe6daa135593230ba470ecbe3d08b0c6337421527ce3027f0fc87125261557a74165342a5c272aeacd7118909eb18f0d8e42f064e4a434bcb23ca1a59bc091259f6e9a4ac7e86ff9024e73bce903724c9e304d689bdf635142eda348197be7e002a7ec2f9b33a57d23cebd7b97bcfe98ac85d46833eef41ace988813464bbe2cefae3e6940fcc1d7a119c1be9b118a8d3beacf8c2e20efc2e68503feb9ba378c783f97b01c09471b6a7e429bd87c6b901f3072df0849ad8c9ee163b34f07af50fc1eecceee9d04fee42f201fdd99d6b03513ece915dc75a01e99fe73b2ab0529e155d6733ee8a03224ed0f3b78832ff8fd7b7cdf622ecfcdf54a273de616d954d75bd9468ab70a965f80d94167f65a'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        if address:
            withoutSpaces = "".join(address.split())
            string = re.sub('[^0-9a-zA-Z]','',withoutSpaces)
            searchString = string.lower()
            command = "mpirun -np 5 python search_address.py " + searchString
            os.system(command)
            with open("results.txt", "r") as f:
                val = len(f.readlines())
            f.close()
            if val == 1:
                flash(f'We had a POSITIVE hit.', 'danger')
                msg =  address + " was found on the OFAC list. DO NOT proceed."
            else:
                flash(f"Your search DID NOT result in any matches.", 'success')
                msg = address + " was NOT found on the OFAC list. You're good to proceed."
        
        if name:
            withoutSpaces = "".join(name.split())
            string = re.sub('[^a-zA-Z]','',withoutSpaces)
            nameString = string.lower()
            command = "mpirun -np 5 python search_name.py " + nameString
            os.system(command)
            with open("resultsN.txt", "r") as f:
                val = len(f.readlines())
            f.close()
            if val == 1:
                flash(f'We had a POSITIVE hit.', 'danger')
                msg =  address + " was found on the OFAC list. DO NOT proceed."
            else:
                flash(f"Your search DID NOT result in any matches.", 'success')
                msg = address + " was NOT found on the OFAC list. You're good to proceed."
        return render_template("results.html", msg=msg, title='Results')        
    return render_template('index.html', title='Search', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/results")
def results():
    return render_template('results.html', title='Results')


if __name__ == '__main__':
    app.run(deubg=True)