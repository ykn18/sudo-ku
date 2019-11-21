package auth

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"strings"
	"time"
)

const secretKey = "some-secret-string"
const layout = "2006-01-02 15:04:05"

type tokenPayload struct {
	Username   string
	Expiration string
}

func decodeToken(payload string) (tokenPayload, error) {
	var tokenBody tokenPayload
	decodedPayload, err := base64.URLEncoding.DecodeString(payload)
	if err != nil {
		return tokenBody, err
	}
	err = json.Unmarshal(decodedPayload, &tokenBody)
	if err != nil {
		return tokenBody, err
	}
	return tokenBody, nil
}

func checkExpiration(expTimestamp string) bool {
	expiration, _ := time.Parse(layout, expTimestamp)
	if time.Now().Before(expiration) {
		return true
	}
	return false
}

func verifySignature(payload string, signature string) bool {
	h := hmac.New(sha256.New, []byte(secretKey))
	h.Write([]byte(payload))
	digest := base64.URLEncoding.EncodeToString(h.Sum(nil))
	if digest == signature {
		return true
	}
	return false
}

/*VerifyToken verifies that the token is valid*/
func VerifyToken(token string) (bool, error) {
	splittedToken := strings.Split(token, ".")
	if verifySignature(splittedToken[0], splittedToken[1]) {
		tokenBody, err := decodeToken(splittedToken[0])
		if err != nil {
			return false, err
		}
		if checkExpiration(tokenBody.Expiration) {
			return true, nil
		}
	}
	return false, nil
}

/*func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter token: ")
	token, _ := reader.ReadString('\n')
	token = strings.Replace(token, "\n", "", 1)
	result, err := VerifyToken(token)
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println("verified:", result)
}*/
