INSERT INTO users(first_name, last_name, email, password) VALUES
('Bob', 'Smith', 'bob.smith@mail.com', 'password123'),
('Mark', 'Johnson', 'mark.johnson@mail.com', 'password1234');

INSERT INTO posts(user_id, title, summary, body, is_deleted) VALUES
(1, 'Charm roof blonde spill hunter', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel ipsum faucibus, vehicula ex sit amet, vehicula ligula. Morbi sed efficitur ex.', 'Donec efficitur tellus eu arcu pellentesque pulvinar. Nullam ut est sed ante fermentum porttitor at sit amet urna. Aliquam tempor felis eu lorem porta feugiat. Sed dapibus mi sit amet magna bibendum, nec mollis lectus ultricies. Nulla lectus est, mollis vel commodo nec, maximus malesuada elit. Suspendisse et arcu cursus, finibus massa tincidunt, pellentesque justo. Ut et venenatis erat.', false),
(1, 'Addition outline law coal sentiment', 'Nulla scelerisque sapien in mi feugiat aliquet. Suspendisse gravida lacus diam, vitae interdum ante consectetur in. Nam maximus lacus id blandit aliquam.', 'Nam ut nisi in risus malesuada lacinia. Aliquam sit amet libero vel nibh molestie tempus at id dui. Nulla fermentum non metus vitae faucibus. Vestibulum lobortis purus quam, vitae placerat nisl porta quis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus porttitor et mi sit amet tincidunt. Cras tristique feugiat tempor.', false),
(2, 'Healthy hope gravity forestry sample', 'Pellentesque egestas scelerisque arcu non pulvinar. Praesent sed elit ipsum. Maecenas efficitur nibh dignissim, dignissim velit eget, hendrerit tellus.', 'Aenean pretium, nibh nec tempor mollis, orci turpis dignissim nisi, eu sollicitudin risus magna in leo. Aenean id eros non ex ultrices maximus. Morbi dignissim nisi imperdiet semper tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec venenatis accumsan euismod. Cras est diam, fringilla at rutrum vel, efficitur non nisi.', false);